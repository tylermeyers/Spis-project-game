
import pygame
import os
import random
import math

#creates screen dimensions
screen_length = 800
screen_height = 600
dim_field = (screen_length, screen_height)

#sets screen equal to the display
#screen = pygame.display.set_mode(dim_field)
screen = pygame.display.set_mode(dim_field)

#sets the background to the background image
background = pygame.image.load(os.path.join("assets", "background1.jpg"))
background = pygame.transform.scale(background, dim_field)
player = pygame.image.load(os.path.join("assets","monkey.png"))
enemy = pygame.image.load(os.path.join("assets", "drug (1).png"))
bulletPic = pygame.image.load(os.path.join("assets", "banana.png"))
bulletPic = pygame.transform.scale(bulletPic, (30, 30))

#variables to use for drawing the PLAYER
playerX = 200
playerY = 200
width = 24
height = 26
playerSpeed = 8
#variables to use for drawing the ENEMY
aiX = 400
aiY = 20
aiWidth = 28
aiHeight = 30
aiSpeed = 3
#variables to use for drawing the bullet
bulletWidth = 30
bulletHeight = 30

#draw the health bars
playerHealthBar = 600
playerHealth = pygame.Rect(0, 0, playerHealthBar, 10)

Boundaries = pygame.sprite.Group()

#creates sprite group for bullet
bullets = pygame.sprite.Group()


class Wall(
        pygame.sprite.Sprite, ):
    def __init__(
        self,
        rb_l,
        rb_t,
        rb_w,
        rb_h,
    ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            os.path.join("assets", "transp.png"))
        self.image = pygame.transform.scale(self.image, (rb_w, rb_h))
        self.rect = self.image.get_rect()
        self.rect.left = rb_l
        self.rect.top = rb_t
        Boundaries.add(self)

wall1 = Wall(187, 0, 561, 112)
wall2 = Wall(187, 190, 462, 137)
wall3 = Wall(180, 112, 7, 78)
wall4 = Wall(757, 115, 10, 262)
wall5 = Wall(263, 326, 10, 40)
wall6 = Wall(130, 360, 133, 5)
wall7 = Wall(79, 500, 142, 5)
wall8 = Wall(222, 500, 10, 40)
wall9 = Wall(237, 540, 400, 10)
wall10 = Wall(607, 400, 160, 10)
wall11 = Wall(607, 394, 5, 69)
wall12 = Wall(607, 460, 137, 5)
wall13 = Wall(746, 464, 5, 136)
wall14 = Wall(640, 550, 5, 50)

class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    #draw rectangle player
    self.image= player
    self.rect = self.image.get_rect()
    self.rect.y = 125
    self.rect.x = 235
    
  def draw(self, background):
    global pcy,pcx
    global ppt
    ppt= self.rect.top
    (pcy,pcx)=(self.rect.y,self.rect.x)
    
  def rotate(self):
    global mx,my # mouse pos x and y
    mx,my = pygame.mouse.get_pos()
    (dx,dy) = (mx- self.rect.centerx), (my - self.rect.centery)
    angle = math.degrees(math.atan2(-dy,dx))- 90

    rot_image = pygame.transform.rotate(self.image,angle)
    rot_image_rect = rot_image.get_rect(center = self.rect.center)

    screen.blit(rot_image,rot_image_rect.topleft)
    
  def update(self):
        #continously moves player down when key is held down
        keys = pygame.key.get_pressed()
        #move left
        if keys[pygame.K_a]:
            #allows player to move as long as player is in the boundaries
            if (self.rect.left <wall3.rect.right and self.rect.top <190 and self.rect.bottom>114) or (self.rect.left < wall2.rect.right and self.rect.top <328 and self.rect.bottom >190) or (self.rect.left < wall5.rect.right and self.rect.top<364 and self.rect.bottom>328) or (self.rect.left < wall8.rect.right and self.rect.top<542 and self.rect.bottom>508) or (self.rect.left < wall14.rect.right and self.rect.top<600 and self.rect.bottom>550) :
              #if self.rect.left>wall1.rect.right and self.rect.bottom >192>111:  #self.rect.left>wall3.rect.right or self.rect.left> wall5.rect.right or self.rect.left> wall8.rect.right or self.rect.left>wall14.rect.right:   
                playerSpeed = 0
                
            else:
                playerSpeed = 8
                self.rect.move_ip(-playerSpeed, 0)
        #move right
        if keys[pygame.K_d]:
            #allows player to move as long as player is in the boundaries
            if (self.rect.right >wall4.rect.left and self.rect.top <378 and self.rect.bottom>117) or (self.rect.right >wall11.rect.left and self.rect.top <465 and self.rect.bottom>403) or (self.rect.right >wall13.rect.left and self.rect.top <600 and self.rect.bottom>466):
                playerSpeed=0
            else:
                playerSpeed = 8
                self.rect.move_ip(playerSpeed, 0)

        #move up
        if keys[pygame.K_w]:
            #allows player to move as long as player is in the boundaries
            if (self.rect.top <wall1.rect.bottom and self.rect.left <748 and self.rect.right>190) or (self.rect.top <wall2.rect.bottom and self.rect.left <650 and self.rect.right>275) or (self.rect.top <wall6.rect.bottom and self.rect.left <274 and self.rect.right>131):
                playerSpeed =0
            else:
                playerSpeed = 8
                self.rect.move_ip(0, -playerSpeed)

        #move down
        if keys[pygame.K_s]:
            #if event.key == pygame.K_DOWN:
            #allows player to move as long as player is in the boundaries
            if (self.rect.bottom <wall2.rect.top and self.rect.left <648 and self.rect.right>275) or (self.rect.bottom >wall10.rect.top and self.rect.left <768 and self.rect.right>613)   :

                playerSpeed = 0
            else:
                playerSpeed = 8
                self.rect.move_ip(0, playerSpeed)

        #make it be able to move diagonally
        if keys[pygame.K_s] and keys[pygame.K_d]:
            if self.rect.bottom < screen_height and self.rect.right < screen_length:
                playerSpeed = 8
                self.rect.move_ip(playerSpeed // 2, playerSpeed // 2)
            else:
                playerSpeed = 0
        if keys[pygame.K_s] and keys[pygame.K_a]:
            if self.rect.bottom < screen_height and self.rect.left > 0:
                playerSpeed = 8
                self.rect.move_ip(-playerSpeed // 2, playerSpeed // 2)
            else:
                playerSpeed = 0
        if keys[pygame.K_w] and keys[pygame.K_d]:
            if self.rect.top > 0 and self.rect.right < screen_length:
                playerSpeed = 8
                self.rect.move_ip(playerSpeed // 2, -playerSpeed // 2)
            else:
                playerSpeed = 0
        if keys[pygame.K_w] and keys[pygame.K_a]:
            if self.rect.top > 0 and self.rect.left > 0:
                playerSpeed = 8
                self.rect.move_ip(-playerSpeed // 2, -playerSpeed // 2)
            else:
                playerSpeed = 0
        
            
          #elif relative_x >0:
            #self.rect.move_ip(-10,0)

        #spawns a new bullet in the bullet group
  def shoot(self):
        bullet = Bullet(self.rect.x + 10, self.rect.y)
        bullets.add(bullet)
#calls player class
playerGrp = Player()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, bulletx, bullety):
        #adds self to sprite group
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletPic
        self.rect = self.image.get_rect() 
        self.rect.x = bulletx
        self.rect.y = bullety
        
    def draw(self):
        #draws bullet on the screen
        screen.blit(self.image, self.rect)

    def update(self):
        
        #get mouse position
        mx, my = pygame.mouse.get_pos()
        #calculate the slope to find the line that the bullet follows
        (rise,run) = (my - pcy, mx - pcx)
        for x in range(0,1):
            #move the bullet according to slope
            self.rect.move_ip(run/10, rise/10)
            #check
            print(self.rect.x,self.rect.y)
            #check
            print("click")

        #gets rid of the bullet from the group when it reaches out of bounds
        if self.rect.bottom < 0 or self.rect.right >screen_length or self.rect.left < 0 or self.rect.bottom>screen_height:
            self.kill()

#enemy class, might want to add health, damage output, starting point, ...
class Enemy(pygame.sprite.Sprite): 
    def __init__(self):
        #adds self to sprite group
        pygame.sprite.Sprite.__init__(self)
        #self.rect = pygame.Rect(aiX, aiY, aiWidth, aiHeight)
        self.image = enemy
        #sets enemy color to blue
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0,427)

    def draw(self):
        #draw enemy on the screen
        screen.blit(self.image, self.rect)

    def update(self):
        #makes enemy trace the player
        aiSpeed = random.randrange(1, 3)
        if(pcx < self.rect.x):
            self.rect.x -= aiSpeed
        if(pcx > self.rect.x):
            self.rect.x += aiSpeed
        if(pcy < self.rect.y):
            self.rect.y -= aiSpeed
        if(pcy > self.rect.y):
            self.rect.y += aiSpeed
        
        #check for collision
        #if(pcx == self.rect.x and pcy == self.rect.y):
            #add fun stuff 
            #print("lost1")
        
        #check for collision with the player
        if (pygame.sprite.spritecollide(playerGrp, enemies, False)):
          #decreases player health
          playerHealth.width -= 1

        #check for collision with the enemy
        if (pygame.sprite.groupcollide(bullets, enemies, True, True)):
          print("collision", self.rect.x)
          
#creates sprite group to store enemy sprites
enemies = pygame.sprite.Group()
#adds  enemy sprites into the group through the use of a forloop
#if enemy <3 and iteration != 5
#+iteration
for i in range(6):
    ai = Enemy()
    enemies.add(ai) 

#create variables for the game loop
clock = pygame.time.Clock()
running = True
FPS = 20
iteration = 0
#Game loop
while running:
    clock.tick(FPS)
    #when key q is pressed, quits the game
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
        #moves when left mouse is clicked
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                playerGrp.shoot()
    
    if len(enemies) < 3 and iteration != 1:
        iteration += 1
        for i in range(6):
            ai = Enemy()
            enemies.add(ai)
        
    #ends the game once player loses all its health
    if playerHealth.width <= 0:
        running = False
        pygame.display.quit()
        os.system('python gameOver.py')
    #ends the game once enemy all dies
    if len(enemies) == 0 and playerGrp.rect.bottom >550:
        running = False
        pygame.display.quit()
        os.system('python transition.py')

    #draws the background
    screen.blit(background, (0, 0))
    #calls the enemy class to draw enemy sprites and makes them move
    playerGrp.draw(screen)
    playerGrp.rotate()
    playerGrp.update()
    enemies.draw(screen)
    enemies.update()
    bullets.draw(screen)
    bullets.update()
    pygame.draw.rect(screen, (0, 255, 0), playerHealth)
    Boundaries.draw(screen)
    pygame.display.update()
