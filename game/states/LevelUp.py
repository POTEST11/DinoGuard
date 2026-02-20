
import pygame
import sys
import json

def levelup():
        
        with open('save data/data.json', 'r') as f:
            data = json.load(f)
    
        current_level = data['current_level']
        unlocked_levels = data['unlocked_levels']
    
        if current_level < 3:
            current_level += 1
            if current_level not in unlocked_levels:
                unlocked_levels.append(current_level)
    
        new_data = {
            "current_level": current_level,
            "unlocked_levels": unlocked_levels,
            "has_save": True
        }
    
        with open('save data/data.json', 'w') as f:
            json.dump(new_data, f, indent=4)

with open('config.json') as f:
    config = json.load(f)

background = pygame.image.load('ASSETS/level_complete.png').convert_alpha()

continue_img = pygame.image.load('ASSETS/button_continue.png').convert_alpha()
continue_img = pygame.transform.scale(continue_img, (200, 50))

continue_rect = continue_img.get_rect(center=(config['WIDTH'] // 2, 450))


def level_up(screen, state_manager):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if continue_rect.collidepoint(event.pos):
                levelup()
                state_manager.change_state("level_page")

    screen.blit(background, (0, 0))
    screen.blit(continue_img, continue_rect)

