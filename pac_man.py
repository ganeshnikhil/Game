import pygame
import sys
import random 


class LudoBoard:
    def __init__(self, screen_width, screen_height, board_size ):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.board_size = board_size
        self.cell_size = self.screen_width // self.board_size
        self.board_position = [[(col * self.cell_size, row * self.cell_size) for col in range(self.board_size)]
                            for row in range(self.board_size)]
        self.colors = {
            "WHITE": (255, 255, 255),
            "PASTEL_RED": (255, 153, 153),
            "PASTEL_GREEN": (153, 255, 153),
            "PASTEL_BLUE": (153, 204, 255),
            "PASTEL_YELLOW": (255, 255, 153),
            "PASTEL_PURPLE": (204, 153, 255)
        }


    def draw_board(self, screen):
        for row in range(self.board_size):
            for col in range(self.board_size):
                x, y = col * self.cell_size, row * self.cell_size
                pygame.draw.rect(screen, self.colors["WHITE"], (x, y, self.cell_size, self.cell_size), 1)

                if (row == 0 or row == 3 or row == 6 or row == 9) and (col == 0 or col == 3 or col == 6 or col == 9):
                    pygame.draw.rect(screen, self.colors["PASTEL_RED"], (x + 1, y + 1, self.cell_size - 2, self.cell_size - 2))
                elif (row == 0 or row == 9) and (2 <= col <= 7):
                    pygame.draw.rect(screen, self.colors["PASTEL_GREEN"], (x + 1, y + 1, self.cell_size - 2, self.cell_size - 2))
                elif (3 <= row <= 6) and (col == 0 or col == 9):
                    pygame.draw.rect(screen, self.colors["PASTEL_BLUE"], (x + 1, y + 1, self.cell_size - 2, self.cell_size - 2))
                else:
                    pygame.draw.rect(screen, self.colors["PASTEL_YELLOW"], (x + 1, y + 1, self.cell_size - 2, self.cell_size - 2))
                    
                    
                    
class enenmy:
   def __init__(self,board_positions):
      self.board_positions = board_positions
      self.color=(255, 0, 0)
      self.radius=20
      self.last_direction_change_time = 0
      self.direction_change_interval = 300  # Change direction every 100 milliseconds
      self.flag = False
      
   def move_ghost(self, ghost_x, ghost_y):
        current_time = pygame.time.get_ticks()
        time_since_last_change = current_time - self.last_direction_change_time

        if time_since_last_change >= self.direction_change_interval:
            if ghost_x + 1 < len(self.board_positions) and self.flag==False:
                ghost_x += 1
                self.flag = True
            elif ghost_x - 1 >= 0 and self.flag==True:
                ghost_x -= 1
                self.flag = False

            # Update the last direction change time
            self.last_direction_change_time = current_time

        return ghost_x, ghost_y
    
   def enemy_draw(self,ghost_x , ghost_y):
      x,y=self.board_positions[ghost_x][ghost_y]
      pygame.draw.circle(screen, self.color, (x + 35, y + 35), self.radius)
   
   @staticmethod
   def collison_detect(ghost_x , ghost_y , player_x , player_y):
      if ghost_x == player_x and ghost_y == player_y:
         return True
      return False
         
      
class Player:
    def __init__(self, board_positions):
        self.x = 0
        self.y = 0
        self.index = 0
        self.radius = 20
        self.color = (0, 0, 0)
        self.board_positions = board_positions

    def move_up(self):
        if self.x - 1 >= 0:
            self.x -= 1

    def move_down(self):
        if self.x + 1 < len(self.board_positions):
            self.x += 1

    def move_left(self):
        if self.y - 1 >= 0:
            self.y -= 1

    def move_right(self):
        if self.y + 1 < len(self.board_positions[0]):
            self.y += 1

    def move_forward(self):
        if self.x - 1 >= 0:
            self.x -= 1
    
    def move_digonal(self):
        if self.x + 1 < len(self.board_positions) and self.y +1 < len(self.board_positions):
            self.x +=1
            self.y +=1
            
            
            
    def move_backward(self):
        if self.x + 1 < len(self.board_positions):
            self.x += 1

    def draw(self, screen):
        x, y = self.board_positions[self.x][self.y]
        pygame.draw.circle(screen, self.color, (x + 35, y + 35), self.radius)

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
# Set up the dimensions of the screen and the board
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
BOARD_SIZE = 10

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ludo Board")

# Create the Ludo board
ludo_board = LudoBoard(SCREEN_WIDTH, SCREEN_HEIGHT, BOARD_SIZE)

# Create the player
player = Player(ludo_board.board_position)
total_ghost=10
def ghost_postion(ludo_board, total_ghosts,player_x , player_y):
    location =[]
    for i in range(total_ghosts):
        x=random.randint(0,len(ludo_board)-1)
        y=random.randint(0,len(ludo_board)-1)
        while(x==player_x and y==player_y or ((x, y) in location)):
            x=random.randint(0,len(ludo_board)-1)
            y=random.randint(0,len(ludo_board)-1)     
        location.append([x,y])
    return location 


ghost_location = ghost_postion(ludo_board.board_position,total_ghost,0,0)

ghost=enenmy(ludo_board.board_position)
delay=0
back_forth=0
#ghost.enemy_draw(ghost_x,ghost_y)
flag=False
# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            elif event.key == pygame.K_DOWN:
                player.move_down()
            elif event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                player.move_right()
            elif event.key == pygame.K_SPACE:
                player.move_digonal()
            #elif event.key == pygame.K_w:
                #player.move_forward()
            #elif event.key == pygame.K_s:
               # player.move_backward()

    # Fill the screen with white color
    screen.fill(ludo_board.colors["WHITE"])

    # Draw the Ludo board
    ludo_board.draw_board(screen)
    # Draw the player
    player.draw(screen)
    player_x , player_y = (player.x , player.y)
    for i,location in enumerate(ghost_location):
        ghost_x , ghost_y = location 
        if ghost.collison_detect(ghost_x,ghost_y,player_x,player_y):
            total_ghost-=1
            ghost_location= ghost_postion(ludo_board.board_position,total_ghost,player_x,player_y)
            
            for location in ghost_location:
                ghost_x , ghost_y = location 
                ghost.enemy_draw(ghost_x,ghost_y)
                
            if total_ghost == 1:
                total_ghost=10
            break
              
                            
        else:
            if delay%100==0:
                if  ghost_x+1  < len(ludo_board.board_position) and flag==False:
                        ghost_location[i][0]=ghost_x+1
                        ghost_x=ghost_x+1
                        #flag=True
                
                elif  ghost_x-1 > 0 and flag==True:
                        ghost_location[i][0]=ghost_x-1
                        ghost_x=ghost_x-1
                        #flag=False
            ghost.enemy_draw(ghost_x,ghost_y)
        
    if delay%100==0:   
        if flag==False:
            flag=True
        else:
            flag= False
                            
                         
    delay+=1
    # Update the screen
    pygame.display.flip()
    clock.tick(60)





