import pygame.font


class Scoreboard():
    '''A class to repot score info'''

    def __init__(self, si_settings, screen, stats):
        '''Initialize scorekeeping attributes.'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.si_settings = si_settings
        self.stats = stats

        # Font settings for scoring informaton.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('resources/Open 24 Display St.ttf', 32)

        # Prepare the Initial score image.
        self.prep_score()
        self.prep_life()


    def prep_score(self):
        '''Turn the score into rendered image.'''
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            f"SCORE : {score_str}", True, self.text_color, self.si_settings.bg_color)

        # Display the score at the top left of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 5


    def show_score(self):
        '''Draw score to the screen.'''
        self.screen.blit(self.score_image, self.score_rect)


    def prep_life(self):
        '''Show life left'''
        self.life_image = pygame.image.load('resources/icons/life.png')
        self.life_rect = self.life_image.get_rect()


    def show_life(self):
        for life in range(self.stats.life_left):
            self.life_rect.right = (
                self.screen_rect.right - 20) - life * (self.life_rect.width + 5)
            self.life_rect.top = 10
            self.screen.blit(self.life_image, self.life_rect)
