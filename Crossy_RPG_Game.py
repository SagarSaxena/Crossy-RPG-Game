# Pygame development 3
# Draw 
#Set up the display

import pygame

pygame.init()

#size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Crossy RPG"
#Colors according to RGB codes (tuples)
WHITE_COLOR = (255, 255, 255) 
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()
TICK_RATE = 60
is_game_over = False

# create window of specified size
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# set background of window to white
game_screen.fill(WHITE_COLOR)
pygame.display.set_caption(SCREEN_TITLE)

player_image = pygame.image.load('player.png')
player_image = pygame.transform.scale(player_image, (50, 50))

# Main game loop, used to update all gameplay such as movement, checks, and graphics
# Runs until is_game_over = True
while not is_game_over:

    # A loop to get all of the events occuring at any given time
    # Events are most often mouse movement, mouse and button clicks, or exit events
    for event in pygame.event.get():
        #If we have a quit type evene,t then exit out of the game loop
        if event.type == pygame.QUIT:
            is_game_over = True
        print(event)

    #pygame.draw.rect(game_screen,BLACK_COLOR, [350, 350, 100, 100])
    #pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)


    game_screen.blit(player_image, (375,375))
        
    # Update all game graphics        
    pygame.display.update()
    # Tick the clock to update eveything within the game
    clock.tick(TICK_RATE)

#Quite pygame and the program
pygame.quit()
quit()
