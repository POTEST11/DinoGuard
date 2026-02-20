import pygame
import sys
import json
import os


    
with open('config.json') as f:
    config = json.load(f)

WIDTH = config['WIDTH']
HEIGHT = config['HEIGHT']

base_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(base_path, '../../ASSETS/background_main.png')).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

controles_img = pygame.image.load(os.path.join(base_path, '../../ASSETS/controls.png')).convert_alpha()
btn_exit = pygame.image.load(os.path.join(base_path, '../../ASSETS/button_exit.png')).convert_alpha()


btn_exit = pygame.transform.scale(btn_exit, (200, 55))
controles_img = pygame.transform.scale(controles_img, (400, 300))



controles_rect = controles_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
btn_exit_rect = btn_exit.get_rect(center=(WIDTH // 2, HEIGHT - 100))


def controles(screen, state_manager):

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                state_manager.change_state("main_menu")

        if event.type == pygame.MOUSEBUTTONDOWN:

            if btn_exit_rect.collidepoint(event.pos):
                state_manager.change_state("main_menu")

    screen.blit(background, (0, 0))

    screen.blit(controles_img, controles_rect)
    screen.blit(btn_exit, btn_exit_rect)



