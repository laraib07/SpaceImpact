import sys
import pygame
import threading
from math import hypot


def check_keydown_event(event, si_settings, screen, player,  stats):
    '''Responce to keypresses.'''
    
    if stats.game_active and player.active:
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

    if event.key == pygame.K_ESCAPE and not stats.game_over:
        if stats.game_active:
            stats.game_active = False
            pygame.mouse.set_visible(True)
        else:
            stats.game_active = True
            pygame.mouse.set_visible(False)

    if event.key == pygame.K_q:
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

    # Draw the play button if the game is inactive
    if not stats.game_active and not stats.game_over:
        play_button.draw_button()

    if stats.game_over:
        restart_button.draw_button()

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

    # make hte most recently drawn screen visible
    pygame.display.flip()


def update_enemy(enemy, player, stats):
    # update enemy position
    if enemy.active:
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

    check_bullet_collision(enemy, player, stats, si_settings, sb)


def check_bullet_collision(enemy, player, stats, si_settings, sb):
    # Check for any bullet that have hit any ship
    # if so get rid of ship and bullet
    enemy_bullet_collision = pygame.sprite.spritecollide(enemy, player.bullets, True)
    player_bullet_collision = pygame.sprite.spritecollide(player, enemy.bullets, True)

    if enemy_bullet_collision:
        stats.score += si_settings.enemy_points
        enemy.explode()
        sb.prep_score()
        enemy.random_position()

    if player_bullet_collision:
        player.explode()
        life_loss(player, enemy,  stats)


def check_player_enemy_collision(player, enemy):
    distance = hypot(player.rect.centerx - enemy.rect.centerx,
                     player.rect.centery - enemy.rect.centery)

    if distance < 50:
        enemy.explode()
        player.explode()
        return True


def life_loss(player, enemy, stats):
    player.active  = False
    enemy.active  = False
    clear = threading.Thread(target=clear_screen, args=(player, enemy,))
    clear.start()

    if stats.life_left > 0:
        stats.life_left -= 1

    else:
        stats.game_active = False
        stats.game_over = True
        pygame.mouse.set_visible(True)


def restart_game(stats, player, enemy, sb):
    stats.reset_stats()
    sb.prep_score()
    clear_screen(player, enemy)
    pygame.mouse.set_visible(False)


def clear_screen(player, enemy):
    player.bullets.empty()
    player.hide()
    enemy.bullets.empty()
    enemy.random_position()
    pygame.time.wait(1000)
    enemy.active = True
    player.active = True
    player.center_ship()
