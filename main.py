import pygame
import os
import pygame.freetype

pygame.font.init()

#creates screen dimensions
screen_length = 1000
screen_height = 800
dim_field = (screen_length, screen_height)

#sets screen equal to the display
screen = pygame.display.set_mode(dim_field)
background = pygame.image.load(os.path.join("assets", "background.jpeg"))
background = pygame.transform.scale(background, dim_field)
decor1 = pygame.image.load(os.path.join("assets", "titleIcon.jpg"))
decor1 = pygame.transform.scale(decor1, (200, 200))

#font
font = pygame.font.Font('freesansbold.ttf', 60)
# create a text surface object which is where text will show
text = font.render('MONKEY RUN', True, (0, 0, 0))
# create a rectangular object for the text surface object
textRect = text.get_rect()
#set the center of the rectangular object and position
textRect.center = (screen_length // 2, screen_height // 3)

#button class
class button():
    def __init__(self, color, x, y, btnWidth, btnHeight, btnText=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = btnWidth
        self.height = btnHeight
        self.text = btnText

    def draw(self, win, outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2,self.y - 2, self.width + 4, self.height + 4), 0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 34)
            btnText = font.render(self.text, 1, (0, 0, 0))
            win.blit(btnText, (self.x + (self.width/2 - btnText.get_width()/2), self.y + (self.height/2 - btnText.get_height()/2)))

    def isOver(self, pos):
        #pos = mouse position
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

#create variables for the game loop
clock = pygame.time.Clock()
running = True
FPS = 20
#draw button
btnPlay = button((200, 200, 0), 300, screen_height // 2, 140, 80, "Let's Play!")
btnHelp = button((255, 204, 153), 550, screen_height // 2, 140, 80, "How To Play")

#Game loop
while running:
    clock.tick(FPS)
    
    #when key q is pressed, quits the game
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if btnPlay.isOver(pos):
                print("btn clicked")
                pygame.display.quit()
                os.system('python backstory.py')

            if btnHelp.isOver(pos):
                print("btn clicked")
                pygame.display.quit()
                os.system('python instructions.py')

#        if event.type == pygame.MOUSEMOTION:
 #           if btnPlay.isOver(pos):
  #              btnPlay.color(100, 100, 100)
   #         else:
    #            btnPlay.color(100, 100, 0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
        
    screen.blit(background, (0, 0))
    screen.blit(text, textRect)
    screen.blit(decor1, (800, 0))
    btnPlay.draw(screen, (0, 0, 0))
    btnHelp.draw(screen, (0, 0, 0))
    pygame.display.update()

