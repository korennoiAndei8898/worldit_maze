import pygame 
import os 

pygame.init()

start_x = 505
start_y = 600

clock = pygame.time.Clock()
display = pygame.display.set_mode((700, 700))
geroina = pygame.Rect(start_x, start_y, 35, 35)

go_right = False
go_left = False
go_up = False
go_down = False

dir_path = os.path.dirname(__file__)
img_path = os.path.abspath(dir_path + "/textures")

floor = pygame.image.load(img_path + "/floor.png")
wall = pygame.image.load(img_path + "/wall.png")
hero = pygame.image.load(img_path + "/hero.png")
hero = pygame.transform.scale(hero, (35,35))
diamond = pygame.image.load(img_path + "/diamond.png")

textures = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
    [1,1,2,2,2,1,1,1,1,1,1,1,1,1], 
    [1,1,2,1,2,1,1,1,1,1,1,1,1,1], 
    [1,1,2,1,2,2,2,2,2,2,4,1,1,1], 
    [1,1,2,1,1,1,2,1,1,1,1,1,1,1], 
    [1,1,2,1,1,1,2,2,2,2,1,1,1,1], 
    [1,1,2,1,1,1,1,1,1,1,1,1,1,1], 
    [1,1,2,2,2,2,2,2,2,2,1,1,1,1], 
    [1,1,2,1,2,1,2,1,1,1,1,1,1,1], 
    [1,1,2,1,2,1,2,2,2,1,1,1,1,1],
    [1,1,2,2,2,1,1,1,2,1,1,1,1,1],
    [1,1,1,1,2,1,1,1,2,2,2,1,1,1],
    [1,1,1,1,2,2,2,2,2,2,2,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1]  
]

rects = [] 
rects_textures = [] 

wall_rects = []
diamond_rects = []

x = 0
y = 0

for texture in textures: 
    for i in texture: 
        kvadrat = pygame.Rect(x, y, 50, 50)
        rects.append(kvadrat)
        rects_textures.append(i)
        if i == 1:
            wall_rects.append(kvadrat)
        if i == 4:
            diamond_rects.append(kvadrat)
        x += 50 
    y += 50
    x = 0

    game = True

while game:

    display.fill((0, 255, 0))
    #pygame.draw.rect(display, (), geroina)

    for i in range(196):
        if rects_textures[i] == 1:
            display.blit(floor, rects[i])
        if rects_textures[i] == 2:
            display.blit(wall, rects[i])
        if rects_textures[i] == 3:
            display.blit(hero, rects[i])
        if rects_textures[i] == 4:
            display.blit(diamond, rects[i])
            
            font = pygame.font.SysFont("Arial", 50)
            text = font.render("YOU WIN!", True, (0,255,0))
        
    display.blit(hero, geroina)

    for bad in wall_rects:
        if geroina.colliderect(bad):
            geroina.x = start_x
            geroina.y = start_y

    for good in diamond_rects:
        if geroina.colliderect(good):
            display.fill((0, 0, 0))
            display.blit(text, (235,200))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                go_right = True
            if event.key == pygame.K_a:
                go_left = True
            if event.key == pygame.K_w:
                go_up = True 
            if event.key == pygame.K_s:
                go_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                go_right = False
            if event.key == pygame.K_a:
                go_left = False
            if event.key == pygame.K_w:
                go_up = False
            if event.key == pygame.K_s:
                go_down = False

    if  go_right == True:
        geroina.x += 5
    if go_left == True:
        geroina.x -= 5
    if go_up == True:
        geroina.y -= 5
    if go_down == True:
        geroina.y += 5

    pygame.display.flip()
    clock.tick(60)