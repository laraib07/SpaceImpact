import pygame
from pygame.sprite import Sprite

class Bullet(Sprite) :
    """A class to manage bullet fired from ship."""

    def __init__(self,si_settings,screen,player) :
        '''Create a bullet object at the palyer's current postion'''
        super(Bullet,self).__init__()
        self.screen = screen

        # create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0,0,si_settings.bullet_width, si_settings.bullet_height)
        self.rect.centery = player.rect.centery
        self.rect.right = player.rect.right

        self.color = si_settings.bullet_color
        self.speed_factor = si_settings.bullet_speed_factor


    def update(self):
        '''Move the bullet right the screen'''
        self.rect.x += self.speed_factor


    def draw_bullet(self):
        '''Draw the bullet to the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)

