import pygame
from pygame import mixer


class Explosion:
    '''Class to animate explosions.'''

    def __init__(self):
        '''Initialize explosion variables.'''
        self.explosion_images = []
        self.explosion_rect = []

        for i in range(9):
            self.image_name = f"resources/explosion-frames/explosion_image_{i}.png"
            self.explosion_images.append(pygame.image.load(self.image_name))
            self.explosion_rect.append(self.explosion_images[i].get_rect())

        self.next_image = 0
        self.do_explode = False
        self.explosion = mixer.Sound('resources/sounds/explosion.wav')


    def explosion_blit(self):
        if self.next_image < len(self.explosion_images):
            self.screen.blit(
                self.explosion_images[self.next_image], self.explosion_rect[self.next_image])
            self.next_image += 1

        else:
            self.next_image = 0
            self.do_explode = False


    def explode(self):
        self.explosion.play()

        for i in range(9):
            self.explosion_rect[i].center = self.rect.center

        self.do_explode = True
