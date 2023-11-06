import pygame
from pygame.locals import RESIZABLE
from driver import master

# window setup

WINDOW_H_base = 637
WINDOW_W_base = 360
displayMultiplier = 1
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
prev_key=pygame.K_ESCAPE
lastpos =0
y_pos = 0
gravity_step = pixelH*0.72*0.5
gravity_timer = 0

#set sprites
bg = pygame.image.load("Assets/board.png")
#shooter = pygame.image.load("Assets/board.png")
pixel = pygame.image.load("Assets/pixel.png")
pixel_purple = pygame.image.load("Assets/pixel_purple.png")
pixel_green = pygame.image.load("Assets/pixel_green.png")
pixel_yellow = pygame.image.load("Assets/pixel_yellow.png")
plusButton = pygame.image.load("Assets/plus.png")
minusButton = pygame.image.load("Assets/minus.png")

#scale sprites
bg = pygame.transform.scale(bg, (realWindowW,realWindowH))
minusButton = pygame.transform.smoothscale(minusButton.convert_alpha(), (30*displayMultiplier,30*displayMultiplier))
plusButton = pygame.transform.smoothscale(plusButton.convert_alpha(), (30*displayMultiplier,30*displayMultiplier))
pixel = pygame.transform.smoothscale(pixel.convert_alpha(), (pixelW,pixelH))
pixel_purple = pygame.transform.smoothscale(pixel_purple.convert_alpha(), (pixelW,pixelH))
pixel_green = pygame.transform.smoothscale(pixel_green.convert_alpha(), (pixelW,pixelH))
pixel_yellow = pygame.transform.smoothscale(pixel_yellow.convert_alpha(), (pixelW,pixelH))


minusRect = minusButton.get_rect()
plusRect = plusButton.get_rect()
pixelRect = pixel.get_rect()

minusRect.center = (100,100)
plusRect.center = (200, 100)

pixel1posX = realWindowW//2-pixelW//2 - 2*(pixelW+realWindowW/450)
pixel1posY = realWindowH-realWindowH//4.75



pixelMatrix = [
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 0 (TOP)
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],             # 1
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 2
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],             # 3
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 4
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 4], [0, 0, 4], [0, 0, 4]],             # 5
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 4], [0, 0, 4], [0, 0, 4], [0, 0, 1]],  # 6
[[0, 0, 0], [0, 0, 0], [0, 0, 4], [0, 0, 4], [0, 0, 1], [0, 0, 1]],             # 7
[[0, 0, 0], [0, 0, 4], [0, 0, 3], [0, 0, 1], [0, 0, 1], [0, 0, 3], [0, 0, 2]],  # 8
[[0, 0, 4], [0, 0, 4], [0, 0, 3], [0, 0, 1], [0, 0, 3], [0, 0, 2]],             # 9
[[pixel1posX-pixelW//2-1.8,pixel1posY-pixelH+realWindowH//44, 1], [0, 0, 3], [0, 0, 3], [0, 0, 3], [0, 0, 2], [0, 0, 3], [0, 0, 3]],  # 10
[[pixel1posX,pixel1posY, 1], [0, 0, 1], [0, 0, 3], [0, 0, 3], [0, 0, 3], [0, 0, 3]],             # 11 (BOTTOM)
]


for j in range(11,0,-2):
    for i in range(0,6):
        pixelMatrix[j][i][0]=pixelMatrix[11][0][0]+(pixelW+1.1)*i
        pixelMatrix[j][i][1]=pixelMatrix[11][0][1]-pixelH*0.72*(11-j)

for j in range(10,-1,-2):
    for i in range(0,7):
        pixelMatrix[j][i][0]=pixelMatrix[10][0][0]+(pixelW+1.1)*i
        pixelMatrix[j][i][1]=pixelMatrix[10][0][1]-(10-j)*pixelH*0.72

px_line7 = list(pixelMatrix[10])
print(px_line7)
px_line6 = list(pixelMatrix[11])
print(px_line6)
        
positions_X = []
positions_Y = []

for i in range(0,13):
    if i%2==0:
        positions_X.append(px_line7[0][0])
        list.pop(px_line7,0)
    else:
        positions_X.append(px_line6[0][0])
        list.pop(px_line6,0)

for i in range(0,12):
    positions_Y.append(pixelMatrix[i][0][1])
#increase rez for y postions
for i in range(len(positions_Y)):
    positions_Y.insert(i+1,(positions_Y[i]+positions_Y[i+1])/2)
    i+=1

print("YGREC")
print(positions_Y)

print(positions_X)
#pixelRect.center = (pixelMatrix[9][1][0],pixelMatrix[9][1][1])
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

    #draw board
    for row in pixelMatrix:
        for pixelProp in row:
            pixelRect.center = (pixelProp[0], pixelProp[1])
            if pixelProp[2]==1:
                screen.blit(pixel, pixelRect)
            elif pixelProp[2]==2:
                screen.blit(pixel_purple, pixelRect)
            elif pixelProp[2]==3:
                screen.blit(pixel_yellow, pixelRect)
            elif pixelProp[2]==4:
                screen.blit(pixel_green, pixelRect)

    

    keys = pygame.key.get_pressed()
    if keys!=prev_key or timer<=0:
        if keys[pygame.K_a]:
            if lastpos!=0: lastpos-=1
        if keys[pygame.K_d]:
            if lastpos!=12: lastpos+=1
        timer=10
    prev_key=keys
    
    player_rect = pixel_green.get_rect()
    player_rect.centerx=positions_X[lastpos]
    player_rect.centery=0+y_pos
    screen.blit(pixel_green, player_rect)
    
    pygame.draw.rect(screen, "black", pygame.Rect(0, 0, realWindowW, realWindowH/20))

    pygame.display.flip()
    timer-=1

    #fall
    
    if gravity_timer>=30:
        y_pos+=gravity_step
        gravity_timer=0
    gravity_timer+=1

    #text
    
    text = master(pixelMatrix, 0)
    font = pygame.font.Font("Arial", 36)
    img1 = font.render(text[0], True, (255, 255, 255))
    img2 = font.render(text[1], True, (255, 255, 255))
    img3 = font.render(text[2], True, (255, 255, 255))
    screen.blit(img1, (30, 290))
    screen.blit(img2, (30, 310))
    screen.blit(img3, (30, 330))

    dt = clock.tick(60) / 1000

pygame.quit()