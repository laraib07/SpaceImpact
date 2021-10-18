import pygame
from pygame.sprite import Sprite
from pygame import mixer


class Bullet(Sprite):
    """A class to manage bullet fired from ship."""

    def __init__(self, si_settings, screen, ship_rect):
        '''Create a bullet object at the palyer's current postion'''
        super(Bullet, self).__init__()
        self.screen = screen

        # create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(
            0, 0, 
            si_settings['bullet']['width'], 
            si_settings['bullet']['height'], 
            )
        self.rect.center = ship_rect.center

        # Play sound when initialized
        fire_sound = mixer.Sound(si_settings['bullet']['sound'])
        fire_sound.play()


    def update(self,speed_factor):
        '''Move the bullet right the screen'''
        self.rect.x += speed_factor


    def draw_bullet(self,color):
        '''Draw the bullet to the screen'''
        pygame.draw.rect(self.screen, color, self.rect)
