import pygame

from si_modules.player import Player
from si_modules.enemy import Enemy
from si_modules.settings import Settings
from si_modules.game_stats import GameStats
from si_modules.button import Button
from si_modules.scoreboard import Scoreboard

import si_modules.game_functions as gf


class SpaceImpact():
    '''
    Class to represent spaceimpact game.
    '''
    def __init__(self):
        # create screen
        self.si_settings = Settings
        self.screen = pygame.display.set_mode(self.si_settings['screen_size'])

        # Title and icon
        pygame.display.set_caption("Space Impact")
        icon = pygame.image.load(self.si_settings['game_icon'])
        pygame.display.set_icon(icon)


        # creating player and  enemy 
        self.player = Player(self.si_settings, self.screen)
        self.enemy = Enemy(self.si_settings, self.screen)

        # Make the Play and Restart button.
        self.play_button = Button(self.screen, "PLAY")
        self.restart_button = Button(self.screen, "RESTART")

        # Create instance to store game stats
        self.stats = GameStats(self.si_settings)
        self.sb = Scoreboard(self.si_settings, self.screen, self.stats)

        # set frames per second
        self.clock = pygame.time.Clock()


    def run(self):
        # game loop
        while True:
            self.clock.tick(30)

            gf.check_events(self)

            if self.stats.game_active:
                self.player.update()
                gf.update_enemy(self.player, self.enemy, self.stats)
                gf.update_bullets(self)

            gf.update_screen(self)


if __name__ == "__main__":
    pygame.init()
    game = SpaceImpact()
    game.run()
    pygame.quit()
