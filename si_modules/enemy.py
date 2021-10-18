import random
import pygame
from pygame.sprite import Group
from si_modules.bullet import Bullet
from si_modules.ship import Ship


class Enemy(Ship):
    '''A class to represent a simple enemy.'''

    def __init__(self, si_settings, screen):
        '''Initialize enemy and set its starting position.'''

        # initialize Ship __init__()
        super().__init__("enemy", si_settings, screen)


        # add bullets color and speed
        self.speed_factor = si_settings.enemy_bullet_speed
        self.color = si_settings.enemy_bullet_color


    def init_position(self):
        self.rect.x = self.screen_rect.right
        self.rect.bottom = random.randint(self.rect.width, self.screen_rect.bottom)


    def update(self):
        '''Move the enemy left.'''
        self.rect.x -= self.si_settings.enemy_speed_factor


    def check_edge(self):
        '''Return True if enemy reached edge of screen.'''
        return self.rect.right <= self.screen_rect.midleft[0]


    def fire_bullet(self):
        # create a  new bullet and add it to th bullets group
        fire = random.choice([False]*30 + [True])
        if fire:
            new_bullet = Bullet(self.si_settings, self.screen, self.rect)
            self.bullets.add(new_bullet)

