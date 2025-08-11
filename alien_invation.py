import sys         # Lets us exit the game cleanly when needed
import pygame      # Main library for making the game window, graphics, and handling events


class AlienInvasion:
    """Overall class that manages game assets and behavior"""  # Description of what this class does
    
    def __init__(self):
        pygame.init()   # Initialize all Pygame modules (graphics, sound, etc.)
        
        # Create the game window with width=1200, height=800 pixels
        self.screen = pygame.display.set_mode((1200, 800))
        
        # Set the title text for the window
        pygame.display.set_caption("Alien Invasion")
    
    
    def run_game(self):
        # Infinite loop that keeps the game running until the user quits
        while True:
            
            # Loop through all recent user interactions/events
            for event in pygame.event.get():
                
                # If the user clicked the close button on the window
                if event.type == pygame.QUIT:
                    sys.exit()  # Exit the program immediately


# Run the game only if this file is executed directly
if __name__ == '__main__':
    ai = AlienInvasion()  # Create an instance of the game
    ai.run_game()         # Start the main game loop
