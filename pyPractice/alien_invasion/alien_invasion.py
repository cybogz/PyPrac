import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
    # Initialize game and create screen object
    pygame.init() # initializes background settings that Pygame needs to work properly.
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # creates a display window called screen
    pygame.display.set_caption("Alien Invasion")

    # make a ship
    ship = Ship(ai_settings, screen)

    # make a group to store bullets in
    bullets = Group()

    #Start the main loop for the game
    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update() # The ships position will update after keyboard events and before screen update
        bullets.update() # calls bullet.update() for each bullet we place in the group bullets
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()