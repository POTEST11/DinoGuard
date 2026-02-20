import pygame
import sys
import json
import os


# Cargar configuración desde JSON con ruta correcta
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../config.json'))
with open(config_path, 'r') as f:
    config = json.load(f)

data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../save data/data.json'))

def reset_save():
    new_data = {
        "current_level": 1,
        "unlocked_levels": [1],
        "has_save": False
    }

    with open(data_path, 'w') as f:
        json.dump(new_data, f, indent=4)

def has_saved_game():
    with open(data_path, 'r') as f:
        data = json.load(f)

    return data['has_save']

WIDTH = config['WIDTH']
HEIGHT = config['HEIGHT']
TITLE = config['TITLE']
FPS = config['FPS']



pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# =========================
# CARGA DE IMÁGENES
# =========================

base_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(base_path, '../../ASSETS/background_main.png')).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

title_img = pygame.image.load(os.path.join(base_path, '../../ASSETS/title.png')).convert_alpha()

btn_nuevo = pygame.image.load(os.path.join(base_path, '../../ASSETS/button_new.png')).convert_alpha()
btn_nuevo = pygame.transform.scale(btn_nuevo, (200, 50))

btn_continuar = pygame.image.load(os.path.join(base_path, '../../ASSETS/button_continue.png')).convert_alpha()
btn_continuar = pygame.transform.scale(btn_continuar, (200, 50))

btn_controles = pygame.image.load(os.path.join(base_path, '../../ASSETS/button_controls.png')).convert_alpha()
btn_controles = pygame.transform.scale(btn_controles, (200, 55))

btn_salir = pygame.image.load(os.path.join(base_path, '../../ASSETS/button_exit.png')).convert_alpha()
btn_salir = pygame.transform.scale(btn_salir, (200, 50))


# =========================
# POSICIONES
# =========================

title_rect = title_img.get_rect(center=(WIDTH // 2, 150))

btn_nuevo_rect = btn_nuevo.get_rect(center=(WIDTH // 2, 360))
btn_continuar_rect = btn_continuar.get_rect(center=(WIDTH // 2, 300))
btn_controles_rect = btn_controles.get_rect(center=(WIDTH // 2, 420))
btn_salir_rect = btn_salir.get_rect(center=(WIDTH // 2, 480))


# =========================
# FUNCIÓN PRINCIPAL MENÚ
# =========================

def main_menu(screen, state_manager):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn_nuevo_rect.collidepoint(event.pos):
                reset_save()
                state_manager.change_state("level_page")

            if btn_controles_rect.collidepoint(event.pos):
                state_manager.change_state("controles")

            if btn_salir_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
            
            if btn_continuar_rect.collidepoint(event.pos) and has_saved_game():
                state_manager.change_state("level_page")


        # Dibujar
        screen.blit(background, (0, 0))
        screen.blit(title_img, title_rect)
        screen.blit(btn_nuevo, btn_nuevo_rect)
        if has_saved_game():
            screen.blit(btn_continuar, btn_continuar_rect)
        screen.blit(btn_controles, btn_controles_rect)
        screen.blit(btn_salir, btn_salir_rect)

        pygame.display.flip()



