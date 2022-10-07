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
font = pygame.font.Font('freesansbold.ttf', 24)
# create a text surface object which is where text will show
text = font.render('One day, there was a monkey. This monkey wished for freedom.', True, (0, 0, 0))
# create a rectangular object for the text surface object
textRect = text.get_rect()
#set the center of the rectangular object and position
textRect.center = (screen_length // 2, 50)
text2 = font.render('But the monkey hunters were out to get him. Now it is TIME!', True, (0, 0, 0))
textRect2 = text.get_rect()
#set the center of the rectangular object and position
textRect2.center = (screen_length // 2, 90)
text3 = font.render('FOR THE GREAT ESCAPE!', True, (0, 0, 0))
textRect3 = text.get_rect()
#set the center of the rectangular object and position
textRect3.center = (screen_length // 2, 130)

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
            font = pygame.font.SysFont('comicsans', 30)
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
btnPlay = button((153, 204, 255), 410, screen_height // 2, 100, 70, "Next")

btnBack = button((252, 168, 168), 280, screen_height // 2, 100, 70, "Back")
#Game loop
while running:
    clock.tick(FPS)
    
    #when key q is pressed, quits the game
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if btnPlay.isOver(pos):
                os.system('python level1.py')
                pygame.display.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if btnBack.isOver(pos):
                pygame.display.quit()
                os.system('python main.py')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
        
    screen.blit(background, (0, 0))
    screen.blit(text, textRect)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    btnPlay.draw(screen, (0, 0, 0))
    btnBack.draw(screen, (0, 0, 0))
    pygame.display.update()

