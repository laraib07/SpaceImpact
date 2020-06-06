import sys
from math import sqrt
import pygame
from si_modules.bullet import Bullet


def check_keydown_event(event, si_settings, screen, player,  stats):
    '''Responce to keypresses.'''
    if stats.game_active:
        if event.key == pygame.K_UP:
            player.moving_up = True

        elif event.key == pygame.K_DOWN:
            player.moving_down = True

        elif event.key == pygame.K_RIGHT:
            player.moving_right = True

        elif event.key == pygame.K_LEFT:
            player.moving_left = True

        elif event.key == pygame.K_SPACE:
            player.fire_bullet()

    if event.key == pygame.K_ESCAPE:
        if stats.game_active:
            stats.game_active = False
            pygame.mouse.set_visible(True)
        else:
            stats.game_active = True
            pygame.mouse.set_visible(False)

    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_event(event, player):
    '''Responce to key releases.'''
    if event.key == pygame.K_UP:
        player.moving_up = False

    elif event.key == pygame.K_DOWN:
        player.moving_down = False

    elif event.key == pygame.K_RIGHT:
        player.moving_right = False

    elif event.key == pygame.K_LEFT:
        player.moving_left = False


def check_events(si_settings, screen, player, enemy, 
                 stats, sb, play_button, restart_button):
    '''Respond to keypresses and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, si_settings, screen,
                                player,  stats)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, player)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_restart_button(stats, restart_button,
                                 mouse_x, mouse_y,  player, enemy, sb)
            check_play_button(stats, play_button, mouse_x, mouse_y)


def check_play_button(stats, play_button, mouse_x, mouse_y):
    '''Start game when the player clicks Play.'''
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_over:
        stats.game_active = True
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)


def check_restart_button(stats, restart_button, mouse_x, mouse_y,  player, enemy, sb):
    '''Start a new game when the player clicks Restart'''
    if restart_button.rect.collidepoint(mouse_x, mouse_y) and stats.game_over:
        restart_game(stats,  player, enemy, sb)


def update_screen(si_settings, screen, player, enemy,
                   stats, play_button, restart_button, sb):
    '''Update images on the screen and flip to the new screen'''
    # Redraw the screen during each pass through the loop
    screen.fill(si_settings.bg_color)

    # Redraw all bullets behind player and enemy
    for bullet in player.bullets.sprites():
        bullet.draw_bullet(player.color)

    for bullet in enemy.bullets.sprites():
        bullet.draw_bullet(enemy.color)

    player.blitme()
    enemy.blitme()

    # Draw the score and life information.
    sb.show_score()
    sb.show_life()

    # Draw the play button if the game is inactive
    if not stats.game_active and not stats.game_over:
        play_button.draw_button()

    if stats.game_over:
        restart_button.draw_button()

    # make hte most recently drawn screen visible
    pygame.display.flip()


def update_enemy(enemy, player, stats):
    # update enemy position
    enemy.update()
    enemy.fire_bullet()

    if enemy.check_edge() or check_player_enemy_collision(player, enemy):
        life_loss(player, enemy,  stats)


def update_bullets(enemy, player, stats, si_settings, sb):
    '''Update bulllets`s position and remove old bullets'''

    # update bullet position
    player.bullets.update(player.speed_factor)
    enemy.bullets.update(enemy.speed_factor)

    
    # Get rid of old bullets
    for bullet in player.bullets.copy():
        if bullet.rect.right > 800:
            player.bullets.remove(bullet)

    for bullet in enemy.bullets.copy():
        if bullet.rect.left <= 0:
            enemy.bullets.remove(bullet)

    check_bullet_enemy_collision(enemy, player, stats, si_settings, sb)
    check_bullet_player_collision(enemy, player, stats, si_settings, sb)


def check_bullet_enemy_collision(enemy, player, stats, si_settings, sb):
    # Check for any bullet that have hit enemy
    # if so get rid of enmy and bullet
    collision = pygame.sprite.spritecollide(enemy, player.bullets, True)

    if collision:
        stats.score += si_settings.enemy_points
        enemy.explosion_sound()
        explosion_animation(enemy)
        sb.prep_score()
        enemy.random_position()


def check_bullet_player_collision(enemy, player, stats, si_settings, sb):
    # Check for any bullet that have hit enemy
    # if so get rid of enmy and bullet
    collision = pygame.sprite.spritecollide(player, enemy.bullets, True)

    if collision:
        # Decrement life value
        stats.life_left -= 1
        player.explosion_sound()
        explosion_animation(player)
        player.center_ship()


def check_player_enemy_collision(player, enemy):
    distance = sqrt(pow(player.rect.centerx - enemy.rect.centerx,
                        2) + pow(player.rect.centery - enemy.rect.centery, 2))
    if distance < 50:
        enemy.explosion_sound()
        explosion_animation(enemy)
        explosion_animation(player)
        return True


def explosion_animation(ship):
    for i in range(9):
        ship.explosion_rect[i].center = ship.rect.center
    ship.explode = True


def life_loss(player, enemy, stats):
    if stats.life_left > 0:
        # Decrement life value
        stats.life_left -= 1
        player.bullets.empty()
        player.center_ship()
        enemy.random_position()

    else:
        enemy.random_position()
        player.center_ship()
        stats.game_active = False
        stats.game_over = True
        pygame.mouse.set_visible(True)


def restart_game(stats, player, enemy, sb):
    stats.reset_stats()
    sb.prep_score()
    player.bullets.empty()
    enemy.random_position()

    # Hide the mouse cursor.
    pygame.mouse.set_visible(False)
