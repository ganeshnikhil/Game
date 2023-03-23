import math 
import random 
import pygame
from pygame import mixer

pygame.init()
ball_xy=[]
ball_y=[]
for i in range(100):
   ball_xy.append((random.randint(100, 500),random.randint(100,300)))
  


screen=pygame.display.set_mode((800,600))
cannon=pygame.image.load("cannon_org.png")
ball=pygame.image.load("ball.png")
ballon=pygame.image.load("ballon.png")
ball_img=pygame.transform.scale(ball,(200,100))
image = pygame.transform.scale(cannon, (100,100))
ballon_img=pygame.transform.scale(ballon,(100,100))
def get_ball_random():
   x=random.randint(100,800)
   y=random.randint(100,600)
   screen.blit(ball_img,(x,y))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 30:
        return True
    else:
        return False
def rot_center(image, angle):
   """rotate an image while keeping its center and size"""
   orig_rect = image.get_rect()
   rot_image = pygame.transform.rotate(image, angle)
   rot_rect = orig_rect.copy()
   rot_rect.center = rot_image.get_rect().center
   rot_image = rot_image.subsurface(rot_rect).copy()
   return rot_image
#screen.blit(cannon, (100, 100))
ballrect=image.get_rect()
running=True
FPS=60
clock=pygame.time.Clock()
speed=[5,5]
degrees=0
distance=0
angle=0
intial_x,intial_y=50,500
new_x,new_y=0,0
flag=False
while running:
   clock.tick(FPS)
    # RGB = Red, Green, Blue
   screen.fill((0, 0, 0))

   screen.blit(ballon_img,ball_xy[0])

   
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      if event.type==pygame.KEYDOWN:
         if event.key==pygame.K_RETURN:
            screen.blit(ballon_img,ball_xy[0])
            traingle_x=abs(ball_xy[0][0]-30)
            traingle_y=abs(ball_xy[0][1]-500)
            
            distance=math.sqrt(((traingle_x)**2+(traingle_y)**2))
            print(traingle_x,traingle_y)
            #angle=math.atan(traingle_y/traingle_x)
            angle=math.atan2(traingle_y,traingle_x)
            degrees=math.degrees(angle)
            
            print(degrees)
            #ball_xy.pop(0)
            flag=True
            #print(angle)
            #rot_center(image,degrees)
            #screen.blit(image,(-20*math.sin(angle),500*math.cos(angle)))
            #rotated_image = pygame.transform.rotate(image, degrees)
            #new_rect = rotated_image.get_rect(center = image.get_rect(center = (-20, 500)).center)
            #screen.blit(rotated_image,new_rect)
            #pygame.display.update()
            #pygame.display.flip()
   rotated_image = pygame.transform.rotate(image, degrees)
   new_rect = rotated_image.get_rect(center = image.get_rect(center = (30, 500)).center)
   screen.blit(rotated_image,new_rect)
   #a=math.radians(angle)
   if isCollision(ball_xy[0][0],ball_xy[0][1],intial_x,intial_y)==False and flag==True:
     intial_x=intial_x+2*math.cos(angle)
     intial_y=intial_y-2*math.sin(angle)
      #intial_x

     
   elif isCollision(ball_xy[0][0],ball_xy[0][1],intial_x,intial_y)==True:
      ball_xy.pop(0)
      intial_x=50
      intial_y=500
   print(intial_x,intial_y)
   #screen.blit(ball_img,(distance*math.cos(angle),distance*math.sin(angle)))
   screen.blit(ball_img,(intial_x,intial_y))
   pygame.display.update()
   #pygame.display.update()