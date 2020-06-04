import sys
import pygame
from si_modules.bullet import Bullet
from si_modules.enemy import Enemy
from time import sleep
from math import sqrt, pow

def check_keydown_event(event,si_settings, screen, player, bullets, stats):
    '''Responce to keypresses.'''
    if event.key == pygame.K_UP :
        player.moving_up = True

    elif event.key == pygame.K_DOWN :
        player.moving_down = True

    elif event.key == pygame.K_RIGHT :
        player.moving_right = True

    elif event.key == pygame.K_LEFT :
        player.moving_left = True

    elif event.key == pygame.K_ESCAPE :
        stats.game_active = False
        pygame.mouse.set_visible(True)

    elif event.key == pygame.K_q:
        sys.exit()

    elif event.key == pygame.K_SPACE :
        fire_bullet(si_settings, screen, player, bullets)


def check_keyup_event(event,player):
    '''Responce to key releases.'''
    if event.key == pygame.K_UP :
        player.moving_up = False

    elif event.key == pygame.K_DOWN :
        player.moving_down = False

    elif event.key == pygame.K_RIGHT :
        player.moving_right = False

    elif event.key == pygame.K_LEFT :
        player.moving_left = False


def check_events(si_settings, screen, player, enemy, bullets, stats, sb, play_button, restart_button) :
    '''Respond to keypresses and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN :
            check_keydown_event(event, si_settings, screen, player, bullets, stats)

        elif event.type == pygame.KEYUP :
            check_keyup_event(event, player)

        elif event.type == pygame.MOUSEBUTTONDOWN :
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_restart_button(stats, restart_button, mouse_x, mouse_y, bullets, player, enemy, sb)
            check_play_button(stats, play_button, mouse_x, mouse_y)


def check_play_button(stats, play_button, mouse_x, mouse_y) :
    '''Start game when the player clicks Play.'''
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_over :
        stats.game_active = True
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)


def check_restart_button(stats, restart_button, mouse_x, mouse_y, bullets, player, enemy, sb):
    '''Start a new game when the player clicks Restart'''
    if restart_button.rect.collidepoint(mouse_x, mouse_y) and stats.game_over :
        restart_game(stats, bullets, player, enemy, sb)


def update_screen(si_settings, screen, player, enemy, bullets, stats, play_button, restart_button, sb):
    '''Update images on the screen and flip to the new screen'''
    # Redraw the screen during each pass through the loop
    screen.fill(si_settings.bg_color)

    # Redraw all bullets behind player and enemy
    for bullet in bullets.sprites():
        bullet.draw_bullet()

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


def update_enemy(si_settings, enemy, player, stats, bullets) :
    # update enemy position
    enemy.update()

    if enemy.check_edge() or check_player_enemy_collision(player, enemy) :
        life_loss(player, enemy, bullets, stats)


def fire_bullet(si_settings, screen, player, bullets):
    # create a  new bullet and add it to th bullets group
    if len(bullets) < si_settings.bullets_allowed :
        new_bullet = Bullet(si_settings, screen, player)
        bullets.add(new_bullet)


def update_bullets(enemy, bullets, stats, si_settings, sb):
    '''Update bulllets`s position and remove old bullets'''

    # update bullet position
    bullets.update()

    # Get rid of old bullets
    for bullet in bullets.copy():
        if bullet.rect.right > 800 :
            bullets.remove(bullet)

    check_bullet_enemy_collision(enemy, bullets, stats, si_settings, sb)


def check_bullet_enemy_collision(enemy, bullets, stats, si_settings, sb) :
    # Check for any bullet that have hit enemy
    # if so get rid of enmy and bullet
    if pygame.sprite.spritecollide(enemy, bullets, True):
        stats.score += si_settings.enemy_points
        sb.prep_score()
        enemy.random_position()


def check_player_enemy_collision(player,enemy):
    distance = sqrt(pow(player.rect.centerx - enemy.rect.centerx,2) + pow(player.rect.centery - enemy.rect.centery, 2))
    return distance < 50



def life_loss(player, enemy, bullets, stats) :
    sleep(0.5)
    if stats.life_left > 1 :
        # Decrement life value
        stats.life_left -= 1
        bullets.empty()
        player.center_ship()
        enemy.random_position()

    else :
        stats.game_active = False
        stats.game_over = True
        pygame.mouse.set_visible(True)


def restart_game(stats, bullets, player, enemy, sb):
    stats.reset_stats()
    sb.prep_score()
    bullets.empty()
    player.center_ship()
    enemy.random_position()

    # Hide the mouse cursor.
    pygame.mouse.set_visible(False)
