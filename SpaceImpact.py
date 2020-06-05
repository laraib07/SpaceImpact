import pygame

from si_modules.player import Player
from si_modules.enemy import Enemy
from si_modules.settings import Settings
from si_modules.game_stats import GameStats
from si_modules.button import Button
from si_modules.scoreboard import Scoreboard

import si_modules.game_functions as gf


def run_game():
    # create screen
    si_settings = Settings()
    screen = pygame.display.set_mode(si_settings.screen_size)

    # Title and icon
    pygame.display.set_caption("Space Impact")
    icon = pygame.image.load(si_settings.game_icon)
    pygame.display.set_icon(icon)


    # creating player and  enemy 
    player = Player(si_settings, screen)
    enemy = Enemy(si_settings, screen)

    # Make the Play and Restart button.
    play_button = Button(screen, "PLAY")
    restart_button = Button(screen, "RESTART")

    # Create instance to store game stats
    stats = GameStats(si_settings)
    sb = Scoreboard(si_settings, screen, stats)

    # set frames per second
    clock = pygame.time.Clock()

    # game loop
    while True:
        clock.tick(30)

        gf.check_events(si_settings, screen, player, enemy,
                         stats, sb, play_button, restart_button)

        if stats.game_active:
            player.update()
            gf.update_enemy(enemy, player, stats)
            gf.update_bullets(enemy, player,  stats, si_settings, sb)

        gf.update_screen(si_settings, screen, player, enemy,
                          stats, play_button, restart_button, sb)


if __name__ == "__main__":
    pygame.init()
    run_game()
    pygame.quit()
