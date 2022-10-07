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
background = pygame.image.load(os.path.join("assets", "victorybg.jpg"))
background = pygame.transform.scale(background, dim_field)

#font
font = pygame.font.Font('freesansbold.ttf', 32)
# create a text surface object which is where text will show
text = font.render('You did it! The earth and your safety are in good hands.', True, (0, 0, 0))
# create a rectangular object for the text surface object
textRect = text.get_rect()
#set the center of the rectangular object and position
textRect.center = (screen_length // 2, 200)

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
btnPlay = button((153, 204, 255), 380, screen_height // 2, 120, 70, "Play again")

btnBack = button((252, 168, 168), 520, screen_height // 2, 100, 70, "Home")
#Game loop
while running:
    clock.tick(FPS)
    
    #when key q is pressed, quits the game
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if btnPlay.isOver(pos):
                pygame.display.quit()
                os.system('python level1.py')

        if event.type == pygame.MOUSEBUTTONDOWN:
            if btnBack.isOver(pos):
                pygame.display.quit()
                os.system('python main.py')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
        
    screen.blit(background, (0, 0))
    screen.blit(text, textRect)
    btnPlay.draw(screen, (0, 0, 0))
    btnBack.draw(screen, (0, 0, 0))
    pygame.display.update()

