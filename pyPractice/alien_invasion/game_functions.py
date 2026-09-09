import sys

import pygame

def check_keydown_events(event, ship):
    """Responds to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True # Move the ship to the right as you hold down key
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True # Move the ship to the left as you hold down key

def check_keyup_events(event, ship):
    """Responds to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False # if you let go of the right key the ship will stop moving
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False # if you let go of the left key the ship will stop moving

def check_events(ship):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen"""
    # Re-draw the screen during each pass through the loop    
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Make the most recently drawn screen visible
    pygame.display.flip()