import pygame
pygame.init()

win = pygame.display.set_mode((1500,600))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('standing2.png'),pygame.image.load('standing3.png'), pygame.image.load('standing2.png'), pygame.image.load('standing.png'),pygame.image.load('standing2.png'), pygame.image.load('standing3.png')]
#walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('BACKGROUND.png')

char = pygame.image.load('standing.png')

x = 50
y = 400
width = 192
height = 192
vel = 20

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    
    win.blit(bg, (0,0))  
    if walkCount + 1 >= 5:
        walkCount = 0
        
    #if left:  
        #win.blit(walkLeft[walkCount//3], (x,y))
        #walkCount += 1                          
    if right:
        win.blit(walkRight[walkCount], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0
        
    pygame.display.update() 
    


run = True

while run:
    clock.tick(9)
    
    #background_image = pygame.image.load("city.png"); #load an image

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 1000 - vel - width:  
        x += vel
        left = False
        right = True
        
    else: 
        left = False
        right = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    redrawGameWindow() 
    
    
    
pygame.quit()