import pygame
from pygame import mixer


class Explosion:
    '''Class to animate explosions.'''

    def __init__(self, screen):
        '''Initialize explosion variables.'''
        self.screen = screen
        self.images = []

        for i in range(9):
            self.img = f"resources/explosion-frames/explosion_image_{i}.png"
            self.images.append(pygame.image.load(self.img))

        self.index = 0
        self.rect = self.images[0].get_rect()
        self._explode = False
        self.explosion = mixer.Sound('resources/sounds/explosion.wav')


    def blit(self):
        if self.index < len(self.images):
            self.screen.blit(
                self.images[self.index], self.rect)
            self.index += 1

        else:
            self.index = 0
            self._explode = False


    def explode(self, other):
        self.explosion.play()
        self.rect.center = other.rect.center
        self._explode = True
