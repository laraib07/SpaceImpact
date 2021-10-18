'''A dictionary to store all settings for Space Impact'''

Settings = {
        'screen_size': (800, 600),
        'bg_color': (36, 32, 55),
        'bg_image': 'resources/icons/background.png',
        'game_icon': 'resources/icons/game_icon.png',
        'font': 'resources/Open 24 Display St.ttf',
        'font_color': (255, 255, 255),

        'player': {
            'speed': 10.0,
            'bullet_speed': 15.0,
            'bullet_color': (226, 24, 0),  # red
            'life': 3,
            'image': 'resources/icons/player.png'
            },

        'enemy': {
            'speed': 12.0,
            'bullet_speed': -15.0,
            'bullet_color': (57, 225, 20),
            'points': 50,
            'image': 'resources/icons/enemy.png'
            },

        'bullet': {
            'width': 15,
            'height': 3,
            'limit': 5,
            'sound': 'resources/sounds/bullet.wav'
            },

        'explosion': {
            'images': [ 
                f"resources/explosion-frames/{i}.png" for i in range(9)
                ],
            'sound': 'resources/sounds/explosion.wav'
            }
        }
