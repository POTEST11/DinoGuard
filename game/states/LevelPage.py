import pygame
import sys
import json
import os

def load_save_data():
    base_path = os.path.dirname(__file__)
    data_path = os.path.abspath(
        os.path.join(base_path, '../../save data/data.json')
    )

    with open(data_path, 'r') as f:
        return json.load(f)
    
with open('config.json') as f:
    config = json.load(f)

WIDTH = config['WIDTH']
HEIGHT = config['HEIGHT']

base_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(base_path, '../../ASSETS/background_main.png')).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

lvl1_img = pygame.image.load(os.path.join(base_path, '../../ASSETS/level1.png')).convert_alpha()
lvl2_img = pygame.image.load(os.path.join(base_path, '../../ASSETS/level2.png')).convert_alpha()
lvl3_img = pygame.image.load(os.path.join(base_path, '../../ASSETS/level3.png')).convert_alpha()
lock_img = pygame.image.load(os.path.join(base_path, '../../ASSETS/lock.png')).convert_alpha()
btn_exit = pygame.image.load(os.path.join(base_path, '../../ASSETS/button_exit.png')).convert_alpha()

lvl1_img = pygame.transform.scale(lvl1_img, (200, 275))
lvl2_img = pygame.transform.scale(lvl2_img, (200, 275))
lvl3_img = pygame.transform.scale(lvl3_img, (200, 275))
lock_img = pygame.transform.scale(lock_img, (50, 50))
btn_exit = pygame.transform.scale(btn_exit, (200, 55))



lvl1_rect = lvl1_img.get_rect(center=(WIDTH // 4, HEIGHT // 2))
lvl2_rect = lvl2_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
lvl3_rect = lvl3_img.get_rect(center=(3 * WIDTH // 4, HEIGHT // 2))
btn_exit_rect = btn_exit.get_rect(center=(WIDTH // 2, HEIGHT - 100))


def level_page(screen, state_manager):

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                state_manager.change_state("main_menu")

        if event.type == pygame.MOUSEBUTTONDOWN:

            if lvl1_rect.collidepoint(event.pos) and 1 in load_save_data()['unlocked_levels']:
                print("Nivel 1")
                state_manager.reset(True)

                state_manager.change_state("gameplay1")

            if lvl2_rect.collidepoint(event.pos) and 2 in load_save_data()['unlocked_levels']:
                print("Nivel 2")
                state_manager.reset(True)
                state_manager.change_state("gameplay2")

            if lvl3_rect.collidepoint(event.pos) and 3 in load_save_data()['unlocked_levels']:
                print("Nivel 3")
                state_manager.reset(True)
                state_manager.change_state("gameplay3")
            if btn_exit_rect.collidepoint(event.pos):
                state_manager.change_state("main_menu")

    screen.blit(background, (0, 0))

    screen.blit(lvl1_img, lvl1_rect)
    screen.blit(lvl2_img, lvl2_rect)
    screen.blit(lvl3_img, lvl3_rect)
    
    screen.blit(btn_exit, btn_exit_rect)

    # Opcional: overlay para bloqueados
    overlay = lock_img.copy()
   

    if 2 not in load_save_data()['unlocked_levels']:
        screen.blit(overlay, lvl2_rect)

    if 3 not in load_save_data()['unlocked_levels']:
        screen.blit(overlay, lvl3_rect)
