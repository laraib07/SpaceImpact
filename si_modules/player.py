import pygame
from pygame.sprite import Group
from si_modules.bullet import Bullet
from si_modules.explosion import Explosion


class Player(Explosion):
    '''A class to represent player.'''

    def __init__(self, si_settings, screen):
        '''Initialize the player and set its starting position.'''
        self.screen = screen
        self.si_settings = si_settings
        
        # initialize explosion __init__()
        super().__init__()

        # Load player image and get its rect
        self.image = pygame.image.load('resources/icons/player.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start the ship at left centre of the screen
        self.center_ship()

        # add bullets
        self.bullets = Group()

        # movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False


    def center_ship(self):
        self.rect.midleft = self.screen_rect.midleft

        # store a decimal value for the player's center.
        self.centery = float(self.rect.centery)
        self.centerx = float(self.rect.centerx)


    def update(self):
        '''Update the player's postion based on movement flag.'''
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.si_settings.player_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.si_settings.player_speed_factor

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.si_settings.player_speed_factor

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.si_settings.player_speed_factor

        # update rect objectfrom self.center
        self.rect.centery = self.centery
        self.rect.centerx = self.centerx


    def blitme(self):
        '''Draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)

        # Show explosion if enemy killed
        if self.explode:
            self.explosion_blit()


    def fire_bullet(self):
    # create a  new bullet and add it to th bullets group
        if len(self.bullets) < self.si_settings.bullets_allowed:
            new_bullet = Bullet(self.si_settings, self.screen, self.rect)
            self.bullets.add(new_bullet)
