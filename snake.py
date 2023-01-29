import pygame
import time
import random
from pygame import mixer
pygame.init()
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,255,0)
blue=(0,0,255)
#width,height=(800,600)
screen=pygame.display.set_mode((800,600))
snake_x=400
snake_y=300
velocity_x=0
velocity_y=0
snake_size=15
food_x=random.randint(100,750)
food_y=random.randint(150,550)
food_size=5
FPS=60
clock=pygame.time.Clock()
over_font = pygame.font.Font('freesansbold.ttf', 64)
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
font = pygame.font.Font('freesansbold.ttf', 32)
score_value=0
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
textX = 10
testY = 10
count=0
def plot_snake(screen,snk_list,sanke_size):
    global count
    for x,y in snk_list:
        count=count+1
        if count%2==0:
            color=green
        else:
            color=red
        pygame.draw.rect(screen,color,[x,y,sanke_size,snake_size])
snk_list=[]
snake_lenght=1
running=True
while running:
    clock.tick(FPS)
    screen.fill(black)
    key=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type== pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
            print('up')
            velocity_x=3
            velocity_y=0
        if event.key==pygame.K_LEFT:
            velocity_x=-3
            velocity_y=0
        if event.key==pygame.K_UP:
            key=True
            velocity_y=-3
            velocity_x=0
        if event.key==pygame.K_DOWN:
            velocity_y=3
            velocity_x=0
    snake_x=snake_x+velocity_x
    snake_y=snake_y+velocity_y
    if max(snake_x,food_x)-min(snake_x,food_x)<=15 and max(snake_y,food_y)-min(snake_y,food_y)<=15:
        bulletSound = mixer.Sound("laser.wav")
        bulletSound.play()
        food_x=random.randint(100,750)
        food_y=random.randint(150,550)
        snake_lenght+=5
        score_value=score_value+1
    if snake_x<=0:
        game_over_sound=mixer.Sound("explosion.wav")
        game_over_sound.play()
        game_over_text()
        time.sleep(0.5)
        break
    elif snake_x>=800:
        game_over_sound=mixer.Sound("explosion.wav")
        game_over_sound.play()
        game_over_text()
        time.sleep(0.5)
        break
    elif snake_y<=0:
        game_over_sound=mixer.Sound("explosion.wav")
        game_over_sound.play()
        game_over_text()
        time.sleep(0.5)
        break
    elif snake_y>=600:
        game_over_sound=mixer.Sound("explosion.wav")
        game_over_sound.play()
        game_over_text()
        time.sleep(0.5)
        break

    pygame.draw.circle(screen,blue,(food_x,food_y),food_size,food_size)
    #pygame.draw.rect(screen,black,[snake_x,snake_y,snake_size,snake_size])
    head=[]
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)
    if len(snk_list)>snake_lenght:
        del snk_list[0]
    if head in snk_list[:-1]:
        if key==False:
            game_over_sound=mixer.Sound("explosion.wav")
            game_over_sound.play()
            game_over_text()
            time.sleep(0.5)
            break
        else:
            pass
    plot_snake(screen,snk_list,snake_size)
    show_score(textX,testY)
    pygame.display.update()