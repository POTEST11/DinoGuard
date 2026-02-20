
import pygame
import sys  
from game.StateManager import StateManager
from game.npcs.npc import NPC 
from game.player import Player
from game.states.MainMenu import main_menu
import json

with open('config.json') as f:
    config = json.load(f)

camera_x = 0


HEIGHT = config['HEIGHT']
WIDTH = config['WIDTH']
NOT_HUEVO = False


background = pygame.image.load('ASSETS/background1.png').convert_alpha()
background = pygame.transform.scale(background, (3000, HEIGHT)) 

floor_block = pygame.image.load('ASSETS/floor_block.png').convert_alpha()
floor_block = pygame.transform.scale(floor_block, (50, 50))

lava_floor = pygame.image.load('ASSETS/lava_floor.png').convert_alpha()
lava_floor = pygame.transform.scale(lava_floor, (50, 50))

lava_block = pygame.image.load('ASSETS/lava_block.png').convert_alpha()
lava_block = pygame.transform.scale(lava_block, (50, 50))

lava_fill = pygame.image.load('ASSETS/lava_fill.png').convert_alpha()
lava_fill = pygame.transform.scale(lava_fill, (50, 50))

sand_block = pygame.image.load('ASSETS/sand.png').convert_alpha()
sand_block = pygame.transform.scale(sand_block, (50, 50))

water_block = pygame.image.load('ASSETS/water.png').convert_alpha()
water_block = pygame.transform.scale(water_block, (50, 50))

huevo_img = pygame.image.load('ASSETS/huevo.png').convert_alpha()
huevo_img = pygame.transform.scale(huevo_img, (50, 50))

dinomom_img = pygame.image.load('ASSETS/dinomom_img.png').convert_alpha()
dinomom_img = pygame.transform.scale(dinomom_img, (70, 90))

dinomom_huevo_img = pygame.image.load('ASSETS/dinomom_huevo_img.png').convert_alpha()
dinomom_huevo_img = pygame.transform.scale(dinomom_huevo_img, (70, 90))

casa_img = pygame.image.load('ASSETS/house.png').convert_alpha()
casa_img = pygame.transform.scale(casa_img, (150, 200))

npc_imageR = pygame.image.load('ASSETS/triceratops_right.png').convert_alpha()
npc_imageL = pygame.image.load('ASSETS/triceratops_left.png').convert_alpha()
npc_imageR = pygame.transform.scale(npc_imageR, (90, 70))
npc_imageL = pygame.transform.scale(npc_imageL, (90, 70))


npc_imageRR = pygame.image.load('ASSETS/raptor_right.png').convert_alpha()
npc_imageRL = pygame.image.load('ASSETS/raptor_left.png').convert_alpha()
npc_imageRR = pygame.transform.scale(npc_imageRR, (40, 60))
npc_imageRL = pygame.transform.scale(npc_imageRL, (40, 60))



player_imageR = pygame.image.load('ASSETS/playerR.png').convert_alpha()
player_imageL = pygame.image.load('ASSETS/playerL.png').convert_alpha()   
player_imageR = pygame.transform.scale(player_imageR, (40, 80))
player_imageL = pygame.transform.scale(player_imageL, (40, 80))

player_huevo = pygame.image.load('ASSETS/player_huevo.png').convert_alpha()
player_huevo = pygame.transform.scale(player_huevo, (50, 90))

player = Player(50, 400, player_imageR, player_imageL, camera_x)








TILE_SIZE = 50
level_map1 = [
    "............................................................",
    "............................................................",
    "............................................................",
    "............................................................",
    "............................................................",
    "............................................................",
    "...........................#.......##.......................",
    ".......###................#b...##........................###",
    "...##.......#............#bb..bbb#.......####...........#bbb",
    "..#b......T.b#..#....T..#bbb..bbb#..T...#bbbb#...T.....#bbbb",
    "##bb########bb..b#####..bbbb..bbbb######bbbbbb#########bbbbb",
    "bbbbbbbbbbbbbb..bbbbbb..bbbb..bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
]

triceratops1 = []

for row_index, row in enumerate(level_map1):
    for col_index, tile in enumerate(row):
        if tile == "T":
            
            triceratops1.append(NPC(col_index * TILE_SIZE, (row_index * TILE_SIZE) +TILE_SIZE, npc_imageR, npc_imageL, 0.5, camera_x))




level_map2 = [
    "............................................................",
    "............................................................",
    "............................................................",
    "............................................................",
    "............................................................",
    "................................LL.................R........",
    ".............................LL................LLLLLL.......",
    "..........................LL.........LL......LLmmmmmmL..L...",
    "................L........Lmm...........LLLLLLmmmmmmmmm..mLLL",
    "....LLLL..R..L..mL...R..Lmmm...........mmmmmmmmmmmmmmm..mmmm",
    "LLLLmmmmLLLLLmllmmLLLLLLmmmmlllllllllllmmmmmmmmmmmmmmm..mmmm",
    "mmmmmmmmmmmmmmllmmmmmmmmmmmmlllllllllllmmmmmmmmmmmmmmm..mmmm",
]

raptops2 = []

for row_index, row in enumerate(level_map2):
    for col_index, tile in enumerate(row):
        if tile == "R":
            raptops2.append(NPC(col_index * TILE_SIZE, (row_index * TILE_SIZE) + TILE_SIZE, npc_imageRR, npc_imageRL, 1.5, camera_x))
                       

level_map3 = [
    "............................................................",
    "............................................................",
    "............................................................",
    "............................................................",
    "............................................................",
    "............................................................",
    "............................PP..............................",
    "...........................PssP.........................PPPP",
    "....PP.......P..P........PPssssPP.......PP.............Pssss",
    "..P.......T.Ps..s.R..P..PssssssssP..T...ssP.....R.....Psssss",
    "PPsPPPPPPPPPss..sPPPPs..ssssssssssPPPPPPssPPPPPPPPPPPPssssss",
    "ssssssssssssssaaasssssaassssssssssssssssssssssssssssssssssss",
]

npcs3 = []

for row_index, row in enumerate(level_map3):
    for col_index, tile in enumerate(row):
        if tile == "R":
            npcs3.append(NPC(col_index * TILE_SIZE, (row_index * TILE_SIZE) + TILE_SIZE, npc_imageRR, npc_imageRL, 2, camera_x))

        if tile == "T":
            npcs3.append(NPC(col_index * TILE_SIZE, (row_index * TILE_SIZE) + TILE_SIZE, npc_imageR, npc_imageL, 0.5, camera_x))



    


def gameplay(screen, state_manager, level, restart):

    if restart:
        player.pos_x = 50
        player.pos_y = 400
        player.rect.topleft = (50, 400)
        state_manager.reset(False)

    if level == 1:
        level_map =  level_map1
        triceratops = triceratops1
    elif level == 2:
        level_map = level_map2
        triceratops = raptops2
    elif level == 3:
        level_map = level_map3
        triceratops = npcs3      
       
    if player.pos_x > WIDTH // 2:
        if player.pos_x <= 3000- (WIDTH // 2):
            camera_x = player.rect.centerx - screen.get_width() // 2
        else: 
            camera_x = 3000 - WIDTH
    else:
        camera_x = 0

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    platforms = []

    screen.blit(background, (0 - camera_x, 0))
    

    for row_index, row in enumerate(level_map):
        for col_index, tile in enumerate(row):
            if tile == "#":
                rect = pygame.Rect(
                    col_index * TILE_SIZE,
                    row_index * TILE_SIZE,
                    TILE_SIZE,
                    TILE_SIZE
                )
                screen.blit(floor_block, (rect.x - camera_x, rect.y))
                platforms.append(rect)  # Guardar el rectángulo para futuras colisiones

            if tile == "L":
                rect = pygame.Rect(
                    col_index * TILE_SIZE,
                    row_index * TILE_SIZE,
                    TILE_SIZE,
                    TILE_SIZE
                )
                screen.blit(lava_floor, (rect.x - camera_x, rect.y))
                platforms.append(rect)  # Guardar el rectángulo para futuras colisiones

            if tile == "l":
                rect = pygame.Rect(
                    col_index * TILE_SIZE,
                    row_index * TILE_SIZE,
                    TILE_SIZE,
                    TILE_SIZE
                )
                screen.blit(lava_block, (rect.x - camera_x, rect.y))
                
            if tile == "m":
                rect = pygame.Rect(
                    col_index * TILE_SIZE,
                    row_index * TILE_SIZE,
                    TILE_SIZE,
                    TILE_SIZE
                )
                screen.blit(lava_fill, (rect.x - camera_x, rect.y))
                platforms.append(rect)  # Guardar el rectángulo para futuras colisiones

            
            if tile == "P":
                rect = pygame.Rect(
                    col_index * TILE_SIZE,
                    row_index * TILE_SIZE,
                    TILE_SIZE,
                    TILE_SIZE
                )
                screen.blit(sand_block, (rect.x - camera_x, rect.y))
                platforms.append(rect)  # Guardar el rectángulo para futuras colisiones

            if tile == "a":
                rect = pygame.Rect(
                    col_index * TILE_SIZE,
                    row_index * TILE_SIZE,
                    TILE_SIZE,
                    TILE_SIZE
                )
                screen.blit(water_block, (rect.x - camera_x, rect.y))
                


            if tile == "b":
                rect = pygame.Rect(
                    col_index * TILE_SIZE,
                    row_index * TILE_SIZE,
                    TILE_SIZE,
                    TILE_SIZE
                )
                pygame.draw.rect(screen, (52, 48, 69), (rect.x - camera_x, rect.y, TILE_SIZE, TILE_SIZE))  # Dibujar un bloque oscuro para representar el bloque de bottom
                platforms.append(rect)  # Guardar el rectángulo para futuras colisiones

            if tile == "s":
                rect = pygame.Rect(
                    col_index * TILE_SIZE,
                    row_index * TILE_SIZE,
                    TILE_SIZE,
                    TILE_SIZE
                )
                pygame.draw.rect(screen, (196, 150, 90), (rect.x - camera_x, rect.y, TILE_SIZE, TILE_SIZE))  # Dibujar un bloque gris para representar el bloque de suelo
                platforms.append(rect)  # Guardar el rectángulo para futuras colisiones


    for npc in triceratops:
        npc.update(platforms)
        npc.draw(screen, camera_x)
        platforms.append(npc.rect)  # Agregar el rectángulo del NPC a la lista de plataformas para colisiones


        

    player.update(platforms)
    player.draw(screen, camera_x)
    if player.pos_x >= 2960:
        state_manager.change_state("level_up")

    if level == 1:
        for npc in triceratops:
            if abs(player.pos_x - npc.rect.centerx) < 90 and abs(player.pos_y - npc.rect.centery) < 100:
                    state_manager.change_state("game_over")



        
        if abs(player.pos_x - (2930)) < 90 and abs(player.pos_y - 300) < 60:
            player.change_image(player_huevo)
        else:
            screen.blit(huevo_img, (2930 - camera_x, 300)) 


    elif level == 2:

        for npc in triceratops:
            if abs(player.pos_x - npc.rect.centerx) < 70 and abs(player.pos_y - npc.rect.centery) < 80:
                    state_manager.change_state("game_over")

        
        if abs(player.pos_x - (2900)) < 100 and abs(player.pos_y - 320) < 60:

            screen.blit(dinomom_huevo_img, (2900 - camera_x, 320))
            
        else:
            screen.blit(dinomom_img, (2920 - camera_x, 320))
            player.change_image(player_huevo) 

    elif level == 3:

        for npc in triceratops:
            if abs(player.pos_x - npc.rect.centerx) < 90 and abs(player.pos_y - npc.rect.centery) < 70:
                    state_manager.change_state("game_over")



        

        screen.blit(casa_img, (2860 - camera_x, 180))
            
             




    if player.pos_y > HEIGHT:
        state_manager.change_state("game_over")


    restart = False



 

