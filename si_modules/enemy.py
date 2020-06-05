import random
import pygame
from pygame import mixer


class Enemy():
    '''A class to represent a simple enemy.'''

    def __init__(self, si_settings, screen):
        '''Initialize enemy and set its starting position.'''
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.si_settings = si_settings

        # Load the enemy image and set its rect attribute
        self.image = pygame.image.load('resources/icons/enemy.png')
        self.explosion = mixer.Sound('resources/sounds/explosion.wav')
        self.rect = self.image.get_rect()

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

    def update(self):
        '''Move the enemy left.'''
        self.rect.x -= self.si_settings.enemy_speed_factor

    def check_edge(self):
        '''Return True if enemy reached edge of screen.'''
        return self.rect.x <= 0

    def explosion_sound(self):
        self.explosion.play()
