import sys
import pygame
import threading
from math import hypot


def check_keydown_event(event, player, stats):
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


def check_events(game):
    '''Respond to keypresses and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, game.player, game.stats)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, game.player)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_restart_button(game, mouse_x, mouse_y)
            check_play_button(game, mouse_x, mouse_y)


def check_play_button(game, mouse_x, mouse_y):
    '''Start game when the player clicks Play.'''
    if game.play_button.rect.collidepoint(mouse_x, mouse_y) and not game.stats.game_over:
        game.stats.game_active = True
        pygame.mouse.set_visible(False)


def check_restart_button(game, mouse_x, mouse_y):
    '''Start a new game when the player clicks Restart'''
    if game.restart_button.rect.collidepoint(mouse_x, mouse_y) and game.stats.game_over:
        restart_game(game)


def update_screen(game):
    '''Update images on the screen and flip to the new screen'''
    # Redraw the screen during each pass through the loop
    game.screen.fill(game.si_settings.bg_color)

    # Draw the play button if the game is inactive
    if not game.stats.game_active and not game.stats.game_over:
        game.play_button.draw_button()

    if game.stats.game_over:
        game.restart_button.draw_button()

    # Redraw all bullets behind player and enemy
    for bullet in game.player.bullets.sprites():
        bullet.draw_bullet(game.player.color)

    for bullet in game.enemy.bullets.sprites():
        bullet.draw_bullet(game.enemy.color)

    game.player.blitme()
    game.enemy.blitme()

    # Draw the score and life information.
    game.sb.show_score()
    game.sb.show_life()

    # make hte most recently drawn screen visible
    pygame.display.flip()


def update_enemy(player, enemy, stats):
    # update enemy position
    if enemy.active:
        enemy.update()
        enemy.fire_bullet()

    if enemy.check_edge() or check_player_enemy_collision(player, enemy):
        life_loss(player, enemy, stats)


def update_bullets(game):
    '''Update bulllets`s position and remove old bullets'''

    # update bullet position
    game.player.bullets.update(game.player.speed_factor)
    game.enemy.bullets.update(game.enemy.speed_factor)

    # Get rid of old bullets
    for bullet in game.player.bullets.copy():
        if bullet.rect.right > game.player.screen_rect.midright[0]:
            game.player.bullets.remove(bullet)

    for bullet in game.enemy.bullets.copy():
        if bullet.rect.left <= game.enemy.screen_rect.midleft[0]:
            game.enemy.bullets.remove(bullet)

    check_bullet_collision(game)


def check_bullet_collision(game):
    # Check for any bullet that have hit any ship
    # if so get rid of ship and bullet
    enemy_bullet_collision = pygame.sprite.spritecollide(game.enemy,
                                                         game.player.bullets,
                                                         True)
    if enemy_bullet_collision:
        game.stats.score += game.si_settings.enemy_points
        game.enemy.explode()
        game.sb.prep_score()
        game.enemy.random_position()

    player_bullet_collision = pygame.sprite.spritecollide(game.player,
                                                          game.enemy.bullets,
                                                          True)
    if player_bullet_collision:
        game.player.explode()
        life_loss(game.player, game.enemy, game.stats)


def check_player_enemy_collision(player, enemy):
    distance = hypot(player.rect.centerx - enemy.rect.centerx,
                     player.rect.centery - enemy.rect.centery)

    if distance < enemy.rect.width:
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


def restart_game(game):
    game.stats.reset_stats()
    game.sb.prep_score()
    pygame.mouse.set_visible(False)


def clear_screen(player, enemy):
    player.bullets.empty()
    player.hide()
    enemy.bullets.empty()
    enemy.random_position()
    pygame.time.wait(1000)
    player.active = True
    player.center_ship()
    pygame.time.wait(1000)
    enemy.active = True
