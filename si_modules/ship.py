import pygame
from abc import ABC, abstractmethod
from pygame.sprite import Group
from si_modules.explosion import Explosion


class Ship(ABC):
    '''Class to represent a ship'''

    def __init__(self, name,  si_settings, screen):
        '''Initialize ship'''
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.si_settings = si_settings

        # Load ship image and its attribute
        self.image = pygame.image.load(
                si_settings[name]['image']
                )
        self.rect = self.image.get_rect()

        # Add bullets
        self.bullets = Group()
        self.speed_factor = si_settings[name]['bullet_speed']
        self.color = si_settings[name]['bullet_color']
        # Start ship and position it 
        self.active = True
        self.init_position()


        # Add explosion variables
        self.explosion = Explosion(screen, si_settings)


    def blitme(self):
        '''Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect)

        # Showxplosion if ship exploded
        if self.explosion._explode:
            self.explosion.blit()

        
    @abstractmethod
    def fire_bullet(self):
        pass


    @abstractmethod
    def init_position(self):
        pass


    @abstractmethod
    def update(self):
        pass
