from pygame import mixer
import pygame
from modules.resources import Resource

class Bullet :
    def __init__(self,screen=None) :
        self.icon = pygame.image.load(Resource.BULLET_ICON)
        self.x = 60
        self.y = 0
        self.speed = 2
        self.state = "READY"
        self.screen = screen

    def render(self):
        self.screen.blit(self.icon, (self.x + 40, self.y + 25))
        self.x += self.speed


    def fire(self):
        bullet_sound = mixer.Sound(Resource.BULLET_SOUND)
        bullet_sound.play()
        self.state = 'FIRE'
        self.screen.blit(self.icon, (self.x + 40, self.y + 30))
