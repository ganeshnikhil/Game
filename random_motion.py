import pygame 
import random 
from pygame import mixer
pygame.init()
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,255,0)
blue=(0,0,255)
screen=pygame.display.set_mode((800,600))
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 100
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 600))
    enemyX_change.append(3)#4
    enemyY_change.append(2)#40

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))
background = pygame.image.load('background.png')
FPS=60
clock=pygame.time.Clock()
running=True
def sound():
    bulletSound = mixer.Sound("laser.wav")
    bulletSound.play()
while running:
    clock.tick(FPS)
    screen.fill(black)
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        enemyY[i]+=enemyY_change[i]
        if enemyX[i] <= 0:

            enemyX_change[i] = 4
            sound()
            enemyX[i]=random.randint(0, 800)
            enemyY[i]=random.randint(50, 600)
            
            #enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 800:
            enemyX_change[i] = -4
            sound()
            enemyX[i]=random.randint(0, 800)
            enemyY[i]=random.randint(50, 600)
            #enemyX_change[i] = -4
            #enemyY[i] += enemyY_change[i]
        elif enemyY[i]<=0:
            enemyY_change[i]=4
            sound()
            enemyX[i]=random.randint(0, 800)
            enemyY[i]=random.randint(50, 600)
            #enemyY_change[i]=4
        elif enemyY[i]>=600:
            enemyY_change[i]=-4
            sound()
            enemyX[i]=random.randint(0, 800)
            enemyY[i]=random.randint(50, 600)
            #enemyY_change[i]=-4
        enemy(enemyX[i],enemyY[i],i)
    pygame.display.update()