import pygame
from modules.resources import Resource

class Player :
    def __init__(self,screen=None) :
        self.image = pygame.image.load(Resource.PLAYER_ICON)
        self.x = 60
        self.y = 268
        self.x_change = 0
        self.y_change = 0
        self.speed = 0.8
        self.screen = screen

    def render(self) :
        self.x += self.x_change
        self.y += self.y_change
        self.screen.blit(self.image,(self.x,self.y))

    def limit_boundary(self) :
        if self.y <= 0 :
            self.y = 0
        elif self.y > 536 :
            self.y = 536

        if self.x <= 0 :
            self.x = 0
        elif self.x > 736 :
            self.x = 736
