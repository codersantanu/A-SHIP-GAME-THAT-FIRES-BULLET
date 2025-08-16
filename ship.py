import pygame
class Ship:
    def __init__(self,ai_game):
        """Initializing sheep and its starting position"""
        self.screen=ai_game.screen
        self.screen_react=ai_game.screen.get_rect()
        
        #Load the ship immage and get its rect.
        self.image=pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale_by(self.image, 0.3)  # shrink to 30% size
        self.rect=self.image.get_rect()
        
        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom=self.screen_react.midbottom
        
        self.moving_right=False # Moving flag
    def update(self):
        if self.moving_right:# Update the ship position based on the movement flag.
            self.rect.x+=1
    def blitme(self):
            """Draw the shit at its current location"""
            self.screen.blit(self.image,self.rect) #blit means "draw" in Pygame.