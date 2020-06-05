import pygame.font


class Button():
    '''A class to represent Buttons.'''

    def __init__(self, screen, msg):
        '''Initialize button attributes.'''
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Se the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (231, 10, 74)
        self.text_color = (36, 32, 55)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's react object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        '''Turn msg into a rendered image ang and center text on the button.'''
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
