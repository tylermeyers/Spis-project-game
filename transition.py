import pygame
import os
import pygame.freetype

pygame.font.init()

#creates screen dimensions
screen_length = 800
screen_height = 600
dim_field = (screen_length, screen_height)

#sets screen equal to the display
screen = pygame.display.set_mode(dim_field)
background = pygame.image.load(os.path.join("assets", "background.jpeg"))
background = pygame.transform.scale(background, dim_field)

#font
font = pygame.font.Font('freesansbold.ttf', 32)
# create a text surface object which is where text will show
text = font.render('You defeated the monkey hunters! But UH OH.', True, (0, 0, 0))
# create a rectangular object for the text surface object
textRect = text.get_rect()
#set the center of the rectangular object and position
textRect.center = (screen_length // 2, 50)
text2 = font.render('After escaping, you fell into an old booby trap', True, (0, 0, 0))
# create a rectangular object for the text surface object
textRect2 = text.get_rect()
#set the center of the rectangular object and position
textRect2.center = (screen_length // 2, 90)
text3 = font.render('that shot you off into space.', True, (0, 0, 0))
# create a rectangular object for the text surface object
textRect3 = text.get_rect()
#set the center of the rectangular object and position
textRect3.center = (screen_length // 2, 130)
text4 = font.render('Good luck decoding these evil robots!', True, (0, 0, 0))
# create a rectangular object for the text surface object
textRect4 = text.get_rect()
#set the center of the rectangular object and position
textRect4.center = (screen_length // 2, 190)

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
            font = pygame.font.SysFont('comicsans', 40)
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
btnPlay = button((200, 200, 0), 360, screen_height // 2, 120, 70, "Let's go")
#Game loop
while running:
    clock.tick(FPS)
    
    #when key q is pressed, quits the game
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if btnPlay.isOver(pos):
                pygame.display.quit()
                os.system('python level2.py')

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
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4, textRect4)
    btnPlay.draw(screen, (0, 0, 0))
    pygame.display.update()

