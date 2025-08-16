import sys              # Lets us exit the game cleanly when needed
import pygame           # Main library for making the game window, graphics, and handling events
from ship import Ship   # Import the Ship class
from settings import Settings   # Import the Setting class


class AlienInvasion:
    """Overall class that manages game assets and behavior"""  # Description of what this class does
    
    def __init__(self):
        pygame.init()   # Initialize all Pygame modules (graphics, sound, etc.)
        self.settings=Settings()
        # Create the game window with
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_hight))
        
        # Set the title text for the window
        pygame.display.set_caption("Alien Invasion")

        self.ship=Ship(self) #from Ship class
    
    def run_game(self):
        # Infinite loop that keeps the game running until the user quits
        while True:
            self._check_event()
            
    def _check_event(self):
            # Loop through all recent user interactions/events
        for event in pygame.event.get():
            # If the user clicked the close button on the window
            if event.type == pygame.QUIT:
                sys.exit()  # Exit the program immediately
                    
            #Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme() 
            
            # Make the most recently drawn screen visible.
            pygame.display.flip()
# Run the game only if this file is executed directly
if __name__ == '__main__':
    ai = AlienInvasion()  # Create an instance of the game
    ai.run_game()         # Start the main game loop
