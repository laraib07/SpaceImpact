import pygame
import  random
import math
from modules.player import Player
from modules.enemy import Enemy
from modules.bullet import Bullet
from modules.resources import Resource,Color

#initialize pygame
pygame.init()

# create screen
size = width,height = 800,600
screen = pygame.display.set_mode(size)

# Title and icon 
pygame.display.set_caption("Space Impact")
icon = pygame.image.load(Resource.GAME_ICON)
pygame.display.set_icon(icon)

# creating player , enemy and bullet
player = Player(screen)
enemy = Enemy(screen)
bullet = Bullet(screen)

# create background image ,initial position and speed
bg = pygame.image.load(Resource.BG_IMAGE)
bg_X = 0
bg_speed = 0.1

# create score board and fonts
score_font = pygame.font.Font(Resource.GAME_FONT,32)
gameover_font = pygame.font.Font(Resource.GAME_FONT,64)
score = 0

def show_score():
    _score = score_font.render(f"Score : {score}",True,Color.WHITE)
    screen.blit(_score,(10,10))


def isCollision(enemy,bullet) :
    distance = math.sqrt(math.pow(enemy.x-bullet.x,2) + math.pow(enemy.y-bullet.y,2))
    return distance < 20

# moving backgroung
def render_bg() :
    global bg_X
    bg_X += bg_speed
    if bg_X > 800 :
        bg_X = 0
    screen.blit(bg,(-bg_X,0))
    screen.blit(bg,(800 - bg_X,0))

def game_over() :
    over_font = gameover_font.render("GAME OVER",True,Color.WHITE)
    screen.blit(over_font,(250,250))


# game loop
running = True
while running :
    screen.fill(Color.STEEL_GREY)
    render_bg()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP :
                player.y_change = -player.speed

            if event.key == pygame.K_DOWN :
                player.y_change = player.speed

            if event.key == pygame.K_RIGHT :
                player.x_change = player.speed

            if event.key == pygame.K_LEFT :
                player.x_change = -player.speed

            if  event.key == pygame.K_SPACE and bullet.state == "READY" :
                bullet.x = player.x
                bullet.y = player.y
                bullet.fire()

        if event.type == pygame.KEYUP :
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN :

                player.y_change = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT :
                player.x_change = 0

    # limiting player movement
    player.limit_boundary()

    if bullet.state == "FIRE" :
        bullet.render()

    if bullet.x > 700 :
        bullet.state = 'READY'

    collision = isCollision(enemy,bullet)
    if collision :
        score += 1
        enemy.explode(bullet)

    if enemy.x < 0 :
        game_over()

    player.render()
    enemy.render()
    show_score()
    pygame.display.update()
