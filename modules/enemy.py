from pygame import mixer
import pygame
import random
from modules.resources import Resource

class Enemy :
    def __init__(self,screen=None) :
        self.image = pygame.image.load(Resource.ENEMY_ICON)
        self.x = 800
        self.y = random.randint(0,536)
        self.x_change = 0
        self.speed = 0.6
        self.screen = screen

    def render(self) :
        self.x -= self.speed
        self.screen.blit(self.image,(self.x,self.y))

    def explode(self,bullet) :
        explosion = mixer.Sound(Resource.ENEMY_EXPLOSION_SOUND)
        explosion.play()
        bullet.x = 60
        bullet.state = "READY"
        self.x = 800
        self.y = random.randint(0,536)
