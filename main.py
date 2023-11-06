import pygame
from pygame.locals import RESIZABLE

# window setup

WINDOW_H_base = 540
WINDOW_W_base = 360
displayMultiplier = 1.5
pixelMultiplier = 0.54

pixelW=83.1*pixelMultiplier*displayMultiplier
pixelH=96.0*pixelMultiplier*displayMultiplier

realWindowH = WINDOW_H_base * displayMultiplier
realWindowW = WINDOW_W_base * displayMultiplier

#game setup
pygame.init()
screen = pygame.display.set_mode((realWindowW,realWindowH))
clock = pygame.time.Clock()
running = True
dt = 0


#set sprites
bg = pygame.image.load("Assets/board.png")
#shooter = pygame.image.load("Assets/board.png")
pixel = pygame.image.load("Assets/pixel.png")
plusButton = pygame.image.load("Assets/plus.png")
minusButton = pygame.image.load("Assets/minus.png")

#scale sprites
bg = pygame.transform.scale(bg, (realWindowW,realWindowH))
minusButton = pygame.transform.smoothscale(minusButton.convert_alpha(), (30*displayMultiplier,30*displayMultiplier))
plusButton = pygame.transform.smoothscale(plusButton.convert_alpha(), (30*displayMultiplier,30*displayMultiplier))
pixel = pygame.transform.smoothscale(pixel.convert_alpha(), (pixelW,pixelH))

minusRect = minusButton.get_rect()
plusRect = plusButton.get_rect()
pixelRect = pixel.get_rect()

minusRect.center = (100,100)
plusRect.center = (200, 100)

pixel1posX = realWindowW//2-pixelW//2 - 2*(pixelW+1.8)
pixel1posY = realWindowH-realWindowH//4.65



player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

pixelMatrix = [
               [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
               [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
               [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
               [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
               [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
               [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
               [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
               [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
               [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
               [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
               [[pixel1posX-pixelW//2-1.8,pixel1posY-pixelH,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
               [[pixel1posX,pixel1posY,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]]

for j in range(11,0,-2):
    for i in range(0,6):
        pixelMatrix[j][i][0]=pixelMatrix[11][0][0]+(pixelW+1.1)*i
        pixelMatrix[j][i][1]=pixelMatrix[11][0][1]

for j in range(10,-1,-2):
    for i in range(0,7):
        pixelMatrix[j][i][0]=pixelMatrix[10][0][0]+(pixelW+1.1)*i
        pixelMatrix[j][i][1]=pixelMatrix[10][0][1]


pixelRect.center = (pixelMatrix[11][1][0],pixelMatrix[11][1][1])
#pixelRect.center = (pixelMatrix[10][0][0],pixelMatrix[10][0][1])

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            if minusRect.collidepoint(event.pos):
                print('minus')
            elif plusRect.collidepoint(event.pos):
                print('plus')

    #set background
    screen.blit(bg, (realWindowW//2-bg.get_width()//2, realWindowH//2-bg.get_height()//2))
    #position ui
    #screen.blit(minusButton, minusRect)
    #screen.blit(plusButton, plusRect)
    screen.blit(pixel,pixelRect)


    """pygame.draw.circle(screen, "black", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt"""

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()