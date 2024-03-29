import pygame
from pygame.sprite import Group
from si_modules.bullet import Bullet
from si_modules.ship import Ship


class Player(Ship):
    '''A class to represent player.'''

    def __init__(self, si_settings, screen):
        '''Initialize the player and set its starting position.'''

        # initialize Ship __init__()
        super().__init__("player", si_settings, screen)


        # initial movement flags set to false
        self.stop_movement()


    def init_position(self):
        self.rect.midleft = self.screen_rect.midleft


    def update(self):
        '''Update the player's postion based on movement flag.'''

        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.si_settings['player']['speed']

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.si_settings['player']['speed']

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.si_settings['player']['speed']

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.si_settings['player']['speed']


    def fire_bullet(self):
        # create a  new bullet and add it to th bullets group
        if len(self.bullets) < self.si_settings['bullet']['limit']:
            new_bullet = Bullet(self.si_settings, self.screen, self.rect)
            self.bullets.add(new_bullet)


    def hide(self):
        self.rect.midright = self.screen_rect.midleft
        self.stop_movement()


    def stop_movement(self):
        # movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False


