import pygame

SCREEN_TITLE = "Crossy RPG"
#size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
#Colors according to RGB codes (tuples)
WHITE_COLOR = (255, 255, 255) 
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()

class Game:
    
    TICK_RATE = 60
    is_game_over = False

    # initializer for game class to set up width, height and title
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # create window of specified size
        self.game_screen = pygame.display.set_mode((width, height))
        # set background of window to white
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False

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
                
            # Update all game graphics        
            pygame.display.update()
            # Tick the clock to update eveything within the game
            clock.tick(self.TICK_RATE)

class GameObject:
    
    def __init__(self, x, y, image_path, width, height):

        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))


pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

#Quit pygame and the program
pygame.quit()
quit()




#pygame.draw.rect(game_screen,BLACK_COLOR, [350, 350, 100, 100])
#pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

#game_screen.blit(player_image, (375,375))
