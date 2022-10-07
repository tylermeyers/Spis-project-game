import pygame
import os
import random
import math

#creates screen dimensions
screen_length = 600
screen_height = 427
dim_field = (screen_length, screen_height)

#sets screen equal to the display
#screen = pygame.display.set_mode(dim_field)
screen = pygame.display.set_mode(dim_field)

#sets the background to the background image
background = pygame.image.load(os.path.join("assets", "background.jpeg"))
background = pygame.transform.scale(background, dim_field)


#variables to use for drawing the PLAYER
playerX = 200
playerY = 200
width = 24
height = 26
playerSpeed = 5
#variables to use for drawing the ENEMY
aiX = 400
aiY = 20
aiWidth = 28
aiHeight = 30
aiSpeed = random.randrange(1, 2)
#variables to use for drawing the bullet
bulletWidth = 10
bulletHeight = 10

#draw rectangle player
#rect_player = pygame.Rect(playerX, playerY, width, height)
#draw the enemy player
#rect_ai = pygame.Rect(aiX, aiY, aiWidth, aiHeight)

#draw the health bars
#global playerHealthBar
playerHealthBar = 200  
playerHealth = pygame.Rect(0, 0, playerHealthBar, 10)
#
#def Health():
#
#create variables for the game loop
clock = pygame.time.Clock()
running = True
FPS = 60
#enemy_im = pygame.image.load(os.path.join("assets", "download (1).jpg"))
class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    #draw rectangle player
    self.image = pygame.Surface((width, height))
    self.image.fill((255, 0, 0))
    self.rect = self.image.get_rect()

    
    #self.rect.x = rect_player.x
    #self.rect.y = rect_player.y

  def draw(self, background):
    global pcy,pcx
    (pcy,pcx)=(self.rect.y,self.rect.x)  
    pt = self.rect.top
    print(pt)
    screen.blit(self.image, self.rect)


  def update(self):
     
     
     #continously moves player down when key is held down
    keys = pygame.key.get_pressed()
    #continuously moves player to the left when key is held down
    if keys[pygame.K_LEFT]:
      #print(type(event))
      if event.key == pygame.K_LEFT:
      #allows player to move as long as player is in the boundaries
        if self.rect.left > 0:
          playerSpeed = 5
          self.rect.move_ip(-playerSpeed, 0)
        else:
          playerSpeed = 0
    #continuously moves player to the right when key is held down
    if keys[pygame.K_RIGHT]:
      if event.key == pygame.K_RIGHT:
        #allows player to move as long as player is in the boundaries
        if self.rect.right < screen_length:
          playerSpeed = 5
          self.rect.move_ip(playerSpeed, 0)
        else:
          playerSpeed = 0

    #continously moves player up when key is held down
    if keys[pygame.K_UP]:
      if event.key == pygame.K_UP:
        #allows player to move as long as player is in the boundaries
        if self.rect.top > 0:
          playerSpeed = 5
          self.rect.move_ip(0, -playerSpeed)
        else:
          playerSpeed = 0

    #continously moves player down when key is held down
    if keys[pygame.K_DOWN]:
      if event.key == pygame.K_DOWN:
        #allows player to move as long as player is in the boundaries
        if self.rect.bottom < screen_height:
          playerSpeed = 5
          self.rect.move_ip(0, playerSpeed)
        else:
          playerSpeed = 0
    
    #make it be able to move diagonally
    if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        if self.rect.bottom < screen_height and self.rect.right < screen_length:
          playerSpeed = 5
          self.rect.move_ip(playerSpeed//2, playerSpeed//2)
        else:
          playerSpeed = 0
    if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        if self.rect.bottom < screen_height and self.rect.left > 0:
          playerSpeed = 5
          self.rect.move_ip(-playerSpeed//2, playerSpeed//2)
        else:
          playerSpeed = 0
    if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        if self.rect.top > 0 and self.rect.right < screen_length:
          playerSpeed = 5
          self.rect.move_ip(playerSpeed//2, -playerSpeed//2)
        else:
          playerSpeed = 0
    if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        if self.rect.top > 0 and self.rect.left > 0:
          playerSpeed = 5
          self.rect.move_ip(-playerSpeed//2, -playerSpeed//2)
        else:
          playerSpeed = 0


#creates sprite group to store player
playerGrp = Player()

#enemy class, might want to add health, damage output, starting point, ...
class Enemy(pygame.sprite.Sprite): 
    
    def __init__(self):
        #adds self to sprite group
        pygame.sprite.Sprite.__init__(self)
        #self.rect = pygame.Rect(aiX, aiY, aiWidth, aiHeight)
        self.image = pygame.Surface((aiWidth, aiHeight))
        #sets enemy color to blue
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0,427)

    def draw(self):
        #pygame.draw.rect(screen, (0,0,255), self.rect)
        screen.blit(self.image, self.rect)

    def update(self):
        if(pcx < self.rect.x):
            self.rect.x -= aiSpeed
        if(pcx > self.rect.x):
            self.rect.x += aiSpeed
        if(pcy < self.rect.y):
            self.rect.y -= aiSpeed
        if(pcy > self.rect.y):
            self.rect.y += aiSpeed
        
        #check for collision
        if(pcx == self.rect.x and pcy == self.rect.y):
            #adjust health bars here in the future
            #add fun stuff 
            print("lost1")
           
        if (pygame.sprite.spritecollide(playerGrp,enemies, False)):
          print("collision", self.rect.x)
          
          #global playerHealthBar
          playerHealth.width -= 3
          #add - health function stuff

#creates sprite group to store enemy sprites
enemies = pygame.sprite.Group()
enemylist = list(enemies)

#adds three enemy sprites into the group through the use of a forloop
for i in range(3):
    ai = Enemy()
    enemies.add(ai) 

class Bullet(pygame.sprite.Sprite):
    def __init__(self,spawn_x,spawn_y):
        #adds self to sprite group
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((bulletWidth, bulletHeight))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        
        #set the bullet x and y equal to the player self.rect.x = 




#Game loop
while running:
    clock.tick(FPS)
    #when key q is pressed, quits the game
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
  

    #hitCheck = pygame.sprite.spritecollide()
    
    
    #draws the background
    screen.blit(background, (0, 0))
    #draws the sprites
    #pygame.draw.rect(screen, (255, 0, 0), rect_player)
    #calls the enemy class to draw enemy sprites and makes them move
    playerGrp.draw(screen)
    playerGrp.update()
    enemies.draw(screen)
    enemies.update()
    #pygame.draw.rect(screen, (0, 0, 255), rect_ai)
    pygame.draw.rect(screen, (0, 255, 0), playerHealth)
    pygame.display.update()
