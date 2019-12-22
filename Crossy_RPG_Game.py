import pygame

SCREEN_TITLE = "Crossy RPG"
#size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
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
        direction = 0

        player_character = PlayerCharacter('ironman.png', 260, 520, 80, 80)
        enemy_0 = EnemyCharacter('thanos.png', 20, 400, 50, 50)
        treasure = GameObject('treasure.png', 260, 50, 80, 80)

        # Mai sn game loop, used to update all gameplay such as movement, checks, and graphics
        # Runs until is_game_over = True
        while not is_game_over:

            # A loop to get all of the events occuring at any given time
            # Events are most often mouse movement, mouse and button clicks, or exit events
            for event in pygame.event.get():

                #If we have a quit type evene,t then exit out of the game loop
                if event.type == pygame.QUIT:
                    is_game_over = True

                # Detect when key is pressed down
                elif event.type == pygame.KEYDOWN:
                    # Move up if up key pressed
                    if event.key == pygame.K_UP:
                        direction = 1
                    # Move down if down key pressed
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                        
                # Detect when key is released
                elif event.type == pygame.KEYUP:
                    # Stop movement when key no longer pressed
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                    
                print(event)

            # redraw screen to be blacnk white window
            self.game_screen.fill(WHITE_COLOR)

            # draw the treasure
            treasure.draw(self.game_screen)

           # draw the player (Ironman)         
            player_character.move(direction, self.height)
            player_character.draw(self.game_screen)

            # draw the enemy (Thanos)
            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)

            if player_character.detect_collision(enemy_0):
                is_game_over = True
            elif player_character.detect_collision(treasure):
                is_game_over = True
                
            # Update all game graphics        
            pygame.display.update()
            # Tick the clock to update eveything within the game
            clock.tick(self.TICK_RATE)

class GameObject:
    
    def __init__(self, image_path, x, y, width, height):

        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    #Draw the object by "blitting" it onto the background
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

# Class to represent the character controlled by the player
class PlayerCharacter(GameObject):

    # How many tiles the character moves per second
    SPEED = 10
    
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Move function move character up if direction > 0 and down if < 0
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        if self.y_pos >= max_height - 80:
            self.y_pos = max_height - 80

    # Return False (no collision) if y positions and x positions do not overlap.
    # Return True if x and positions of player and other_body overlap
    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False

        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos +self.width < other_body.x_pos:
            return False

        return True

# Class to represent the enemy
class EnemyCharacter(GameObject):

    # How many tiles the character moves per second
    SPEED = 10
    
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Move function will move 
    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 20:
            self.SPEED = -abs(self.SPEED)

        self.x_pos += self.SPEED

            
pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

#Quit pygame and the program
pygame.quit()
quit()




#pygame.draw.rect(game_screen,BLACK_COLOR, [350, 350, 100, 100])
#pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

#game_screen.blit(player_image, (375,375))
