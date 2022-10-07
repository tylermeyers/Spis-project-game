import pygame
import os
import random
import math

#creates screen dimensions
screen_length = 1000
screen_height = 800
dim_field = (screen_length, screen_height)

#sets screen equal to the display
#screen = pygame.display.set_mode(dim_field)
screen = pygame.display.set_mode(dim_field)

#sets the background to the background image
background = pygame.image.load(os.path.join("assets", "spacebg.png"))
background = pygame.transform.scale(background, dim_field)
player = pygame.image.load(os.path.join("assets", "monkeySpace.png"))
enemy = pygame.image.load(os.path.join("assets", "robot.png"))
enemy = pygame.transform.scale(enemy, (70, 70))
bulletPic = pygame.image.load(os.path.join("assets", "apsBullet.png"))
bulletPic = pygame.transform.scale(bulletPic, (30, 50))

#player speed variable
playerSpeed = 8
#enemy speed variable
aiSpeed = 3

#draw the health bars
playerHealthBar = 750
playerHealth = pygame.Rect(0, 0, playerHealthBar, 10)

#draw enemy health bars
#enemyHealth = pygame.Rect(600, 0, 40, 10)

#creates sprite group for bullet
bullets = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    #draw rectangle player
    self.image = player
    self.rect = self.image.get_rect()

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
        if self.rect.left > 0:
          playerSpeed = 8
          self.rect.move_ip(-playerSpeed, 0)
        else:
          playerSpeed = 0
    #move right
    if keys[pygame.K_d]:
        #allows player to move as long as player is in the boundaries
        if self.rect.right < screen_length:
          playerSpeed = 8
          self.rect.move_ip(playerSpeed, 0)
        else:
          playerSpeed = 0

    #move up
    if keys[pygame.K_w]:
        #allows player to move as long as player is in the boundaries
        if self.rect.top > 0:
          playerSpeed = 8
          self.rect.move_ip(0, -playerSpeed)
        else:
          playerSpeed = 0

    #move down
    if keys[pygame.K_s]:
      #if event.key == pygame.K_DOWN:
        #allows player to move as long as player is in the boundaries
        if self.rect.bottom < screen_height:
          playerSpeed =8
          self.rect.move_ip(0, playerSpeed)
        else:
          playerSpeed = 0
    
    #make it be able to move diagonally
    if keys[pygame.K_s] and keys[pygame.K_d]:
        if self.rect.bottom < screen_height and self.rect.right < screen_length:
          playerSpeed = 8
          self.rect.move_ip(playerSpeed//2, playerSpeed//2)
        else:
          playerSpeed = 0
    if keys[pygame.K_s] and keys[pygame.K_a]:
        if self.rect.bottom < screen_height and self.rect.left > 0:
          playerSpeed = 8
          self.rect.move_ip(-playerSpeed//2, playerSpeed//2)
        else:
          playerSpeed = 0
    if keys[pygame.K_w] and keys[pygame.K_d]:
        if self.rect.top > 0 and self.rect.right < screen_length:
          playerSpeed = 8
          self.rect.move_ip(playerSpeed//2, -playerSpeed//2)
        else:
          playerSpeed = 0
    if keys[pygame.K_w] and keys[pygame.K_a]:
        if self.rect.top > 0 and self.rect.left > 0:
          playerSpeed = 8
          self.rect.move_ip(-playerSpeed//2, -playerSpeed//2)
        else:
          playerSpeed = 0

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

        #gets rid of the bullet from the group when it reaches out of bounds
        if self.rect.bottom < 0 or self.rect.right >screen_length or self.rect.left < 0 or self.rect.bottom>screen_height:
            self.kill()

#enemy class, might want to add health, damage output, starting point, ...
class Enemy(pygame.sprite.Sprite):
   
    def __init__(self):
        #adds self to sprite group
        pygame.sprite.Sprite.__init__(self)
        #sets enemy color to blue
        self.image = enemy
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 750)
        self.rect.y = random.randrange(0, 550)
        
    def draw(self):
        #draw enemy on the screen
        screen.blit(self.image, self.rect)
        
    def update(self):
        #makes enemy trace the player
        #randomizes ai speed range
        aiSpeed = random.randrange(1, 3)
        if(pcx < self.rect.x):
            self.rect.x -= aiSpeed
        if(pcx > self.rect.x):
            self.rect.x += aiSpeed
        if(pcy < self.rect.y):
            self.rect.y -= aiSpeed
        if(pcy > self.rect.y):
            self.rect.y += aiSpeed
        
        #check for collision with the player
        if (pygame.sprite.spritecollide(playerGrp, enemies, False)):
          #decreases player health
          playerHealth.width -= 3

        if (pygame.sprite.groupcollide(bullets, enemies, True, True)):
          print("collision", self.rect.x)
          
#creates sprite group to store enemy sprites
enemies = pygame.sprite.Group()
#adds  enemy sprites into the group through the use of a forloop - spawns new enemies in waves
for i in range(5):
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

    if len(enemies) < 3 and iteration != 3:
        iteration += 1
        for i in range(7):
            ai = Enemy()
            enemies.add(ai)

    #ends the game once player loses all its health
    if playerHealth.width <= 0:
        running = False
        pygame.display.quit()
        os.system('python gameOver.py')
    #ends the game once player wins
    if len(enemies) == 0:
        running = False
        pygame.display.quit()
        os.system('python victoryOver.py')

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
    pygame.display.update()
