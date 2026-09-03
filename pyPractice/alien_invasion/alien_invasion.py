import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game and create screen object
    pygame.init() # initializes background settings that Pygame needs to work properly.
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # creates a display window called screen
    pygame.display.set_caption("Alien Invasion")

    # make a ship
    ship = Ship(ai_settings, screen)

    #Start the main loop for the game
    while True:

        gf.check_events(ship)
        ship.update() # The ships position will update after keyboard events and before screen update
        gf.update_screen(ai_settings, screen, ship)

run_game()