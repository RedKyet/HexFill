import pygame
from pygame.locals import RESIZABLE
from driver import get_stats
from driver import bomb
import random
import math

import copy

# window setup

pygame.display.set_caption('Hexfill')
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
x_pos = 6
gravity_step = pixelH*0.72*0.5
gravity_timer = 0
velocity = 3


#set sprites
bg = pygame.image.load("Assets/board.png")
#shooter = pygame.image.load("Assets/board.png")
pixel = pygame.image.load("Assets/pixel.png")
pixel_purple = pygame.image.load("Assets/pixel_purple.png")
pixel_green = pygame.image.load("Assets/pixel_green.png")
pixel_yellow = pygame.image.load("Assets/pixel_yellow.png")
plusButton = pygame.image.load("Assets/plus.png")
bomba = pygame.image.load("Assets/bomb.png")
minusButton = pygame.image.load("Assets/minus.png")

#scale sprites
bg = pygame.transform.scale(bg, (realWindowW,realWindowH))
minusButton = pygame.transform.smoothscale(minusButton.convert_alpha(), (30*displayMultiplier,30*displayMultiplier))
plusButton = pygame.transform.smoothscale(plusButton.convert_alpha(), (30*displayMultiplier,30*displayMultiplier))
pixel = pygame.transform.smoothscale(pixel.convert_alpha(), (pixelW,pixelH))
pixel_purple = pygame.transform.smoothscale(pixel_purple.convert_alpha(), (pixelW,pixelH))
pixel_green = pygame.transform.smoothscale(pixel_green.convert_alpha(), (pixelW,pixelH))
pixel_yellow = pygame.transform.smoothscale(pixel_yellow.convert_alpha(), (pixelW,pixelH))
bomba = pygame.transform.smoothscale(bomba.convert_alpha(), (pixelW,pixelH))

player_sprite = pixel
sprites = (pixel,pixel_yellow,pixel_purple,pixel_green,bomba)
sprites_nobomb = (pixel,pixel_yellow,pixel_purple,pixel_green)

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
[[0, 0, 0], [0, 0, 4], [0, 0, 2], [0, 0, 1], [0, 0, 1], [0, 0, 2], [0, 0, 3]],  # 8
[[0, 0, 4], [0, 0, 4], [0, 0, 2], [0, 0, 1], [0, 0, 2], [0, 0, 3]],             # 9
[[pixel1posX-pixelW//2-1.8,pixel1posY-pixelH+realWindowH//44, 1], [0, 0, 2], [0, 0, 2], [0, 0, 2], [0, 0, 3], [0, 0, 2], [0, 0, 2]],  # 10
[[pixel1posX,pixel1posY, 1], [0, 0, 1], [0, 0, 2], [0, 0, 2], [0, 0, 2], [0, 0, 2]],             # 11 (BOTTOM)
]

pixelMatrix = [
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 0 (TOP)
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],             # 1
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 2
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],             # 3
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 4
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],             # 5
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 6
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],             # 7
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 8
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],             # 9
[[pixel1posX-pixelW//2-1.8,pixel1posY-pixelH+realWindowH//44, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  # 10
[[pixel1posX,pixel1posY, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],             # 11 (BOTTOM)
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
for j in range(2):
    i=0
    while(i<len(positions_Y)-1):
        positions_Y.insert(i+1,(positions_Y[i]+positions_Y[i+1])/2)
        i+=2

for i in range(10):
    positions_Y.insert(0,positions_Y[0]-(positions_Y[1]-positions_Y[0]))

y_pos = 0
print("YGREC")
print(positions_Y)

print(positions_X)
#pixelRect.center = (pixelMatrix[9][1][0],pixelMatrix[9][1][1])
#pixelRect.center = (pixelMatrix[10][0][0],pixelMatrix[10][0][1])

prev_score = 0

#update score
score_mat = copy.deepcopy(pixelMatrix)
text = get_stats(score_mat, pixelMatrix, prev_score)

font = pygame.font.Font("Assets\\AvenirLTStd-Black.otf", 12)
big_font = pygame.font.Font("Assets\\AvenirLTStd-Black.otf", 20)
img1 = big_font.render(text[0][0], True, (255, 255, 255))
img2 = font.render(text[0][1], True, (255, 255, 255))
if(text[2] == 2):
    img3 = font.render(text[0][2], True, (254, 223, 3))
elif(text[2] == 3):
    img3 = font.render(text[0][2], True, (156, 141, 184))
elif(text[2] == 4):
    img3 = font.render(text[0][2], True, (149, 232, 16))
else:
    img3 = font.render(text[0][2], True, (255, 255, 255))

prev_score = text[1]

while running:

    # bomb
    # bomb(pixelMatrix, [x, y, color])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        """if event.type == pygame.MOUSEBUTTONUP:
            if minusRect.collidepoint(event.pos):
                print('minus')
            elif plusRect.collidepoint(event.pos):
                print('plus')"""

    #set background
    screen.blit(bg, (realWindowW//2-bg.get_width()//2, realWindowH//2-bg.get_height()//2))
    #position ui
    """
    screen.blit(minusButton, minusRect)
    screen.blit(plusButton, plusRect)"""


    """#check if pixel can be placed
    if(y_pos==len(positions_Y)-1-2*4):
        if x_pos%2==1:
            pixelMatrix[9][x_pos//2][2] = 2"""

    for row in pixelMatrix:
        for pixelProp in row:
            pixelRect.center = (pixelProp[0], pixelProp[1])
            if pixelProp[2]==1:
                screen.blit(pixel, pixelRect)
            elif pixelProp[2]==3:
                screen.blit(pixel_purple, pixelRect)
            elif pixelProp[2]==2:
                screen.blit(pixel_yellow, pixelRect)
            elif pixelProp[2]==4:
                screen.blit(pixel_green, pixelRect)
            elif pixelProp[2]==5:
                screen.blit(bomba, pixelRect)
        

    keys = pygame.key.get_pressed()
    if keys!=prev_key or timer<=0:
        if keys[pygame.K_a]:
            if x_pos!=0: x_pos-=1
        if keys[pygame.K_d]:
            if x_pos!=12: x_pos+=1
        timer=10
    prev_key=keys
    
    player_rect = player_sprite.get_rect()
    player_rect.centerx=positions_X[x_pos]
    player_rect.centery=positions_Y[y_pos]
    print(y_pos)
    screen.blit(player_sprite, player_rect)
    
    pygame.draw.rect(screen, "black", pygame.Rect(0, 0, realWindowW, realWindowH/20))

    timer-=1

    #fall
    
    if gravity_timer>=velocity:
        y_pos+=1
        gravity_timer=0
    gravity_timer+=1

    #pixel placed

    def respawn():
        global y_pos
        global x_pos
        global player_sprite
        global img1
        global img2
        global img3
        global prev_score

        y_pos=0
        x_pos=random.randrange(0,len(positions_X))
        player_sprite = random.choice((random.choice(sprites),random.choice(sprites_nobomb),random.choice(sprites_nobomb),random.choice(sprites_nobomb),random.choice(sprites_nobomb),random.choice(sprites_nobomb),random.choice(sprites_nobomb)))
        


        #update score
        score_mat = copy.deepcopy(pixelMatrix)
        text = get_stats(score_mat, pixelMatrix, prev_score)
        
        img1 = big_font.render(text[0][0], True, (255, 255, 255))
        
        if(text[3] == False):
            img2 = font.render(text[0][1], True, (255, 255, 255))
        else:
            img2 = font.render(text[0][1], True, (252, 3, 73))
            
        if(text[2] == 2):
            img3 = font.render(text[0][2], True, (254, 223, 3))
        elif(text[2] == 3):
            img3 = font.render(text[0][2], True, (156, 141, 184))
        elif(text[2] == 4):
            img3 = font.render(text[0][2], True, (149, 232, 16))
        else:
            img3 = font.render(text[0][2], True, (255, 255, 255))
            
        prev_score = text[1]


    print((y_pos-2)/4+1)
    print('ypos')
    print(math.trunc((y_pos-10)/4+1))

    y_posInMatrix=math.trunc((y_pos-10)/4)
    if y_posInMatrix+1<12 and y_posInMatrix+1>=0:
        if y_posInMatrix%2==0:
            if x_pos==0 and pixelMatrix[y_posInMatrix+1][(x_pos+1)//2][2]:
                pixelMatrix[y_posInMatrix][x_pos//2][2] = sprites.index(player_sprite)+1
                respawn()
            elif x_pos==12 and pixelMatrix[y_posInMatrix+1][(x_pos-1)//2][2]:
                pixelMatrix[y_posInMatrix][x_pos//2][2] = sprites.index(player_sprite)+1
                respawn()
            elif pixelMatrix[y_posInMatrix+1][(x_pos-1)//2][2] and pixelMatrix[y_posInMatrix+1][(x_pos+1)//2][2]:
                print("YES")
                pixelMatrix[y_posInMatrix][x_pos//2][2] = sprites.index(player_sprite)+1
                respawn()
            elif x_pos!=12 and x_pos!=0 and x_pos%2==0 and pixelMatrix[y_posInMatrix+1][(x_pos)//2][2]:
                x_pos+=random.choice((-1,1))
            elif x_pos!=12 and x_pos!=0 and pixelMatrix[y_posInMatrix+1][(x_pos-1)//2][2] :
                x_pos+=1
            elif x_pos!=12 and x_pos!=0 and pixelMatrix[y_posInMatrix+1][(x_pos)//2][2]:
                x_pos-=1
        else:
            if x_pos<=1 and pixelMatrix[y_posInMatrix+1][(x_pos+1)//2][2] and pixelMatrix[y_posInMatrix+1][(x_pos+2)//2][2]:
                pixelMatrix[y_posInMatrix][x_pos//2][2] = sprites.index(player_sprite)+1
                respawn()
            elif x_pos>=11 and pixelMatrix[y_posInMatrix+1][(x_pos-1)//2][2] and pixelMatrix[y_posInMatrix+1][(x_pos-2)//2][2]:
                pixelMatrix[y_posInMatrix][(x_pos-1)//2][2] = sprites.index(player_sprite)+1
                respawn()
            elif pixelMatrix[y_posInMatrix+1][(x_pos-1)//2][2] and pixelMatrix[y_posInMatrix+1][(x_pos+1)//2][2]:
                print("YES")
                pixelMatrix[y_posInMatrix][x_pos//2][2] = sprites.index(player_sprite)+1
                respawn()
            elif x_pos!=12 and x_pos!=0 and x_pos%2==1 and pixelMatrix[y_posInMatrix+1][(x_pos)//2][2]:
                x_pos+=random.choice((-1,1))
            elif x_pos!=12 and x_pos!=0 and pixelMatrix[y_posInMatrix+1][(x_pos)//2][2]:
                x_pos+=1
            elif x_pos!=12 and x_pos!=0 and pixelMatrix[y_posInMatrix+1][(x_pos+1)//2][2]:
                x_pos-=1

    else:
        if y_pos>=len(positions_Y) and x_pos%2==1:
            pixelMatrix[11][x_pos//2][2] = sprites.index(player_sprite)+1
            respawn()
        elif y_pos>=len(positions_Y)-2 and x_pos%2==0:
            if x_pos == 0 or pixelMatrix[11][x_pos//2-1][2] and x_pos != 12:
                pixelMatrix[11][x_pos//2][2] = sprites.index(player_sprite)+1
            elif x_pos == 12 or pixelMatrix[11][x_pos//2][2] and x_pos != 0:
                pixelMatrix[11][x_pos//2-1][2] = sprites.index(player_sprite)+1
            elif x_pos !=12 and x_pos!=0:
                pixelMatrix[11][random.choice((x_pos//2-1,x_pos//2))][2] = sprites.index(player_sprite)+1
            respawn()


        

    screen.blit(img1, (30, 550))
    screen.blit(img2, (30, 580))
    screen.blit(img3, (30, 595))
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000
    

pygame.quit()