import random
import pygame
from pygame.sprite import Group
from si_modules.bullet import Bullet
from si_modules.explosion import Explosion


class Enemy(Explosion):
    '''A class to represent a simple enemy.'''

    def __init__(self, si_settings, screen):
        '''Initialize enemy and set its starting position.'''
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.si_settings = si_settings

        # initialize explosion __init__()
        super().__init__()  

        # Load the enemy image and set its rect attribute
        self.image = pygame.image.load('resources/icons/enemy.png')
        self.rect = self.image.get_rect()

        # add bullets
        self.bullets = Group()
        self.speed_factor = si_settings.enemy_bullet_speed
        self.color = si_settings.enemy_bullet_color

        # Start each enemy at random position
        self.random_position()

        # Store the enemy's exact position
        self.x = float(self.rect.x)


    def random_position(self):
        self.rect.x = self.screen_rect.right
        self.rect.bottom = random.randint(100, self.screen_rect.bottom)


    def blitme(self):
        '''Draw the enemy at its current location.'''
        self.screen.blit(self.image, self.rect)

        # Show explosion if enemy killed
        if self.do_explode:
            self.explosion_blit()


    def update(self):
        '''Move the enemy left.'''
        self.rect.x -= self.si_settings.enemy_speed_factor


    def check_edge(self):
        '''Return True if enemy reached edge of screen.'''
        return self.rect.x <= 0

    
    def fire_bullet(self):
    # create a  new bullet and add it to th bullets group
        fire = random.choice([False]*30 + [True])
        if fire:
            new_bullet = Bullet(self.si_settings, self.screen, self.rect)
            self.bullets.add(new_bullet)

