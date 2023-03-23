import math 
import random 
import pygame
from pygame import mixer
import time
#intialize pygame library
pygame.init()
#intialize a list ball_xy to store the coordinate of x and y
ball_xy=[]
#genrate random x and y coordinates for ballon 
for i in range(100):
   ball_xy.append((random.randint(100, 500),random.randint(100,300)))
 #create a font 
font = pygame.font.Font('freesansbold.ttf', 32)
#intialize the screen size
screen=pygame.display.set_mode((800,600))
#load the image of cannon 
cannon=pygame.image.load("cannon_org.png")
#laod the image of bullet
ball=pygame.image.load("ball.png")
#load the image of target 
ballon=pygame.image.load("ballon.png")
#resize the image of bullet
ball_img=pygame.transform.scale(ball,(40,40))
#resize the image of cannon 
image = pygame.transform.scale(cannon, (300,100))
#resize the image of target 
ballon_img=pygame.transform.scale(ballon,(100,100))

#genrate random postion of x and y coodinates of bullet
#it is not used in this program we are using intial ball_xy list values to random postion of target
'''def get_ball_random():
   x=random.randint(100,800)
   y=random.randint(100,600)
   screen.blit(ball_img,(x,y))'''
   
#function uses distance formula to check for collison s
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(bulletX - enemyX, 2) + (math.pow(bulletY - enemyY, 2)))
   
    if distance<27:
        return True
    else:
        return False



#create a rectangle 
ballrect=image.get_rect()
#ruuning is true 
running=True
#intialize the frame per sec to 50
FPS=50
#intilaize the clock speed
clock=pygame.time.Clock()
#intialize the degress for degreee angle 
degrees=0
#intilize distane variable
distance=0
#intialize angel for radian as angle 
angle=0

#intilize the bullet x and y coordinates 
bullet_x,bullet_y=50,475
#intialize the cannon x and y coordiantes
cannon_x,cannon_y=50,500
#intialize a flag to false it is used to time lapse between the collisions
flag=False

#intialize a color value 
color=(0,255,0)
#intilize a list to store the trail of bullet 
trail=[]
while running:
   #sync the clock with frame per sec 
   clock.tick(FPS)
    # RGB = Red, Green, Blue
   #fill the screen with blackbackground 
   screen.fill((0, 0, 0))
   #use pygames event keys 
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
   
   #get the distance of  x coordiante of target from cannon 
   traingle_x=abs(ball_xy[0][0]-cannon_x)
   #get the distance of y coodinate of target form cannon 
   traingle_y=abs(ball_xy[0][1]-cannon_y)
   #calculate the distane b/w them using distance formula       
   distance=math.sqrt(((traingle_x)**2+(traingle_y)**2))
   print(traingle_x,traingle_y)
            #angle=math.atan(traingle_y/traingle_x)
   #use tan inverse get the anlge b/w them 
   angle=math.atan2(traingle_y,traingle_x)
   #convert angle in degress
   degrees=math.degrees(angle)
   #use intialize fornt to show the anlge on screen 
   score=font.render("angle:"+str(round(degrees)),True,(255,255,0))
   #show it to screen at given coordiantes 
   screen.blit(score,(560,530)) 
      
   print(degrees)
         
   #if colliosn of bullet and target have not occured 
   if isCollision(ball_xy[0][0],ball_xy[0][1],bullet_x,bullet_y)==False:
     #change x coordiante of bullet using motion in 2-d formula 
     bullet_x=bullet_x+5*math.cos(angle)
      #change the y coordinates of bullet using motion in 2-d fourmula 
     bullet_y=bullet_y-5*math.sin(angle)
   #append the new bullets coordinate to trail list intialize earlier
     trail.append((bullet_x,bullet_y))
     print(trail)
   #calculate new distance bullet get after changing ther coordinate 
     dist=math.sqrt(bullet_x**2+bullet_y**2)
     #run loop for lenghth of trail 
     for i in range(len(trail)):
         #render the distance of new bullet x and y on screen at given coordiantes 
         dis=font.render("distance:"+str(dist),True,(0,255,255))
         screen.blit(dis,(560,560))
         #change the color of trail to create dot pattern behind 
         if i%2==0 and i!=0:
            pygame.draw.rect(screen,color,pygame.Rect(trail[i][0],trail[i][1]+30,3,3))
         else:
            pygame.draw.rect(screen,(0,0,0),pygame.Rect(trail[i][0],trail[i][1]+30,3,3))

    
   #intilize falg to false for time lapse after bullet hit the target 
     flag=False
    #if collison ocuurs 
   elif isCollision(ball_xy[0][0],ball_xy[0][1],bullet_x,bullet_y)==True:
      #use quick laser sound for short interaval 
      explosionSound = mixer.Sound("laser.wav")
      explosionSound.play()
      #delte the intial coodinates 
      ball_xy.pop(0)
      #bullet gets back to it's intial coordinates bullet_x and bullet_y intialized after collison 
      bullet_x=50
      bullet_y=475
      #intialize degrees to zero so cannon get back to it's intial postion 
      degrees=0
      #intialize flag is equal to true 
      flag=True
      #empty the trail so new coodinates of bullet stored.
      trail=[]

   #rotate cannon to desired angle for shooting the target 
   rotated_image = pygame.transform.rotate(image, degrees)
   new_rect = rotated_image.get_rect(center = image.get_rect(center = (cannon_x, cannon_y)).center)
   screen.blit(rotated_image,new_rect)
   print(bullet_x,bullet_y)
   #screen.blit(ball_img,(distance*math.cos(angle),distance*math.sin(angle)))
   #time.sleep(0.01111111111111)
   #show the bulllet on screen 
   screen.blit(ball_img,(bullet_x,bullet_y))
   #show target on screen
   screen.blit(ballon_img,ball_xy[0])
   #update the graphics of screen after each iteration 
   pygame.display.update()
   #wait for sec after bullet hit the target . wait after collison 
   if flag:
      time.sleep(0.9)
   
   #time.sleep(0.5)
   #pygame.display.update()
