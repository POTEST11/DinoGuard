import pygame
import sys
import json
from game.StateManager import StateManager
from game.states.MainMenu import main_menu
from game.states.LevelPage import level_page
from game.states.Gameplay import gameplay
from game.states.LevelUp import level_up
from game.states.GameOver import game_over
from game.states.Controles import controles

with open('config.json') as f:
    config = json.load(f)

WIDTH = config['WIDTH']
HEIGHT = config['HEIGHT']
TITLE = config['TITLE']
FPS = config['FPS']

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

state_manager = StateManager()

running = True


while running:
    dt = clock.tick(FPS)

    if state_manager.current_state == "main_menu":
        main_menu(screen, state_manager)

    elif state_manager.current_state == "level_page":
        level_page(screen, state_manager)

    elif state_manager.current_state == "level_up":
    
        level_up(screen, state_manager)

    elif state_manager.current_state == "game_over":
        
        game_over(screen, state_manager)

    elif state_manager.current_state == "gameplay1":
        gameplay(screen, state_manager, 1, state_manager.restart)

    elif state_manager.current_state == "gameplay2":
        gameplay(screen, state_manager, 2, state_manager.restart)

    elif state_manager.current_state == "gameplay3":
        gameplay(screen, state_manager, 3, state_manager.restart) 

    elif state_manager.current_state == "controles":
        controles(screen, state_manager)

    elif state_manager.restart == "restart":
       state_manager.reset(True)

        

    pygame.display.flip()
