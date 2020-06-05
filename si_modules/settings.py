

class Settings:
    '''A class to store all settings for Space Impact'''

    def __init__(self):
        '''initialize game's settings.'''

        # screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (36, 32, 55)
        self.bg_image = 'resources/icons/background.png'
        self.game_icon = 'resources/icons/game_icon.png'

        # fonts
        self.font = 'resources/Open 24 Display St.ttf'
        self.font_color = (255, 255, 255)

        # player speed
        self.player_speed_factor = 10.0
        self.player_limit = 3

        # enemy speed
        self.enemy_speed_factor = 8.0
        self.enemy_points = 50

        # bullet settings
        self.bullet_speed_factor = 15
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (226, 24, 0)   # red
        self.bullets_allowed = 5
