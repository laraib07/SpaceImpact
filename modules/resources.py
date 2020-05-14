import os

class Resource :
    # PWD :- Present Working Directory
    PWD = os.path.dirname(os.path.realpath(__file__))

    GAME_ICON = os.path.join(f'{PWD}/../','resources/icons/game_icon.png')
    GAME_FONT = os.path.join(f'{PWD}/../','resources/Open 24 Display St.ttf')
    BG_IMAGE = os.path.join(f'{PWD}/../','resources/icons/background.png')

    # player resources
    
    PLAYER_ICON = os.path.join(f'{PWD}/../','resources/icons/player.png')

    # enemy resources
    ENEMY_ICON = os.path.join(f'{PWD}/../','resources/icons/enemy.png')
    ENEMY_EXPLOSION_SOUND = os.path.join(f'{PWD}/../','resources/sounds/explosion.wav')

    # bullet resources
    BULLET_ICON = os.path.join(f'{PWD}/../','resources/icons/bullet.png')
    BULLET_SOUND = os.path.join(f'{PWD}/../','resources/sounds/bullet.wav')

class Color :
    WHITE = (255,255,255)
    STEEL_GREY = (36,32,55)
