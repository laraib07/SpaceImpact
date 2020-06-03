class GameStats():
    '''Track statistics for Space Impact.'''

    def __init__( self, si_settings ) :
        '''Initialize stats'''
        self.si_settings = si_settings
        self.reset_stats()


    def reset_stats(self) :
        '''Initialize stat that can change during game.'''
        self.life_left = self.si_settings.player_limit
        self.score = 0

        # Start Game in inactive state
        self.game_active = False
        self.game_over = False


