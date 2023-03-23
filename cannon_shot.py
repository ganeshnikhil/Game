import math 
import random 
import pygame
from pygame import mixer
import time
pygame.init()
ball_xy=[]
ball_y=[]
for i in range(100):
   ball_xy.append((random.randint(100, 500),random.randint(100,300)))
  
font = pygame.font.Font('freesansbold.ttf', 32)

screen=pygame.display.set_mode((800,600))
cannon=pygame.image.load("cannon_org.png")
ball=pygame.image.load("ball.png")
ballon=pygame.image.load("ballon.png")
ball_img=pygame.transform.scale(ball,(40,40))
image = pygame.transform.scale(cannon, (300,100))
ballon_img=pygame.transform.scale(ballon,(100,100))


def get_ball_random():
   x=random.randint(100,800)
   y=random.randint(100,600)
   screen.blit(ball_img,(x,y))
   
   
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(bulletX - enemyX, 2) + (math.pow(bulletY - enemyY, 2)))
   
    if distance<27:
        return True
    else:
        return False



#screen.blit(cannon, (100, 100))
ballrect=image.get_rect()
running=True
FPS=50
clock=pygame.time.Clock()

degrees=0
distance=0
angle=0
#intial_x,intial_y=80,486

#intial_x,intial_y=75,486
bullet_x,bullet_y=50,475
cannon_x,cannon_y=50,500
flag=False
#screen.blit(ballon_img,ball_xy[0])
color=(0,255,0)
trail=[]
while running:
   clock.tick(FPS)
    # RGB = Red, Green, Blue
   screen.fill((0, 0, 0))
   #screen.blit(background, (0, 0))
   #screen.blit(ballon_img,ball_xy[0])
   
   #time.sleep(0.4444)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      #if event.type==pygame.KEYDOWN:
         #if event.key==pygame.K_RETURN:

   traingle_x=abs(ball_xy[0][0]-cannon_x)
   traingle_y=abs(ball_xy[0][1]-cannon_y)
            
   distance=math.sqrt(((traingle_x)**2+(traingle_y)**2))
   print(traingle_x,traingle_y)
            #angle=math.atan(traingle_y/traingle_x)
   angle=math.atan2(traingle_y,traingle_x)
   degrees=math.degrees(angle)
   
   score=font.render("angle:"+str(round(degrees)),True,(255,255,0))
   screen.blit(score,(560,530)) 
      
   print(degrees)
            #ball_xy.pop(0)

            #print(angle)
            #rot_center(image,degrees)
            #screen.blit(image,(-20*math.sin(angle),500*math.cos(angle)))
            #rotated_image = pygame.transform.rotate(image, degrees)
            #new_rect = rotated_image.get_rect(center = image.get_rect(center = (-20, 500)).center)
            #screen.blit(rotated_image,new_rect)
            #pygame.display.update()
            #pygame.display.flip()
   #rotated_image = pygame.transform.rotate(image, degrees)
   #new_rect = rotated_image.get_rect(center = image.get_rect(center = (30, 500)).center)
   #screen.blit(rotated_image,new_rect)
   #a=math.radians(angle)
   #trail=[]
   if isCollision(ball_xy[0][0],ball_xy[0][1],bullet_x,bullet_y)==False:
      
     bullet_x=bullet_x+5*math.cos(angle)
     bullet_y=bullet_y-5*math.sin(angle)
     trail.append((bullet_x,bullet_y))
     print(trail)
     dist=math.sqrt(bullet_x**2+bullet_y**2)
     for i in range(len(trail)):
         dis=font.render("distance:"+str(dist),True,(0,255,255))
         screen.blit(dis,(560,560))
         if i%2==0 and i!=0:
            pygame.draw.rect(screen,color,pygame.Rect(trail[i][0],trail[i][1]+30,3,3))
         else:
            pygame.draw.rect(screen,(0,0,0),pygame.Rect(trail[i][0],trail[i][1]+30,3,3))

     #dist=math.sqrt(bullet_x**2+bullet_y**2)
     #dis=font.render("distance:"+str(dist),True,(0,0,0))
     #screen.blit(dis,(560,560))
     flag=False
      #intial_x
   elif isCollision(ball_xy[0][0],ball_xy[0][1],bullet_x,bullet_y)==True:
      explosionSound = mixer.Sound("laser.wav")
      explosionSound.play()
      
      ball_xy.pop(0)
      bullet_x=50
      bullet_y=475
      degrees=0
      #pygame.Sprite.kill(ballon_img)
      #screen.blit(ballon_img,(700,0))
      flag=True
      #trail=[]

     
   rotated_image = pygame.transform.rotate(image, degrees)
   new_rect = rotated_image.get_rect(center = image.get_rect(center = (cannon_x, cannon_y)).center)
   screen.blit(rotated_image,new_rect)
   print(bullet_x,bullet_y)
   #screen.blit(ball_img,(distance*math.cos(angle),distance*math.sin(angle)))
   #time.sleep(0.01111111111111)
   screen.blit(ball_img,(bullet_x,bullet_y))
   screen.blit(ballon_img,ball_xy[0])
   pygame.display.update()
   if flag:
      #screen.blit(ballon_img,ball_xy[0])
      time.sleep(0.9)
   
   #time.sleep(0.5)
   #pygame.display.update()