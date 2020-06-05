import pygame
from pygame import mixer


class Explosion:

    def __init__(self):

        self.explosion_images = []
        self.explosion_rect = []
        for i in range(9):
            self.image_name = f"resources/explosion-frames/explosion_image_{i}.png"
            self.explosion_images.append(pygame.image.load(self.image_name))
            self.explosion_rect.append(self.explosion_images[i].get_rect())

        self.next_image = 0
        self.explode = False
        self.explosion = mixer.Sound('resources/sounds/explosion.wav')

    def explosion_blit(self):
        if self.next_image < len(self.explosion_images):
            self.screen.blit(
                self.explosion_images[self.next_image], self.explosion_rect[self.next_image])
            self.next_image += 1
            self.tick = pygame.time.get_ticks()

        else:
            self.next_image = 0
            self.explode = False


    def explosion_sound(self):
        self.explosion.play()
