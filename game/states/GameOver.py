

import pygame
import sys
import json


with open('config.json') as f:
    config = json.load(f)

background = pygame.image.load('ASSETS/game_over.png').convert_alpha()

salir_img = pygame.image.load('ASSETS/button_exit.png').convert_alpha()
salir_img = pygame.transform.scale(salir_img, (200, 50))

salir_rect = salir_img.get_rect(center=(config['WIDTH'] // 2, 520))


def game_over(screen, state_manager):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if salir_rect.collidepoint(event.pos):
                state_manager.change_state("main_menu")

    screen.blit(background, (0, 0))
    screen.blit(salir_img, salir_rect)