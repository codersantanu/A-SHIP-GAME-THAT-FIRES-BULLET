import pygame
class Ship:
    def __init__(self,ai_game):
        """Initializing sheep and its starting position"""
        self.screen=ai_game.screen
        self.screen_react=ai_game.screen.get_rect()
        
        #Load the ship immage and get its rect.
        self.image=pygame.image.load('image/ship.bmp')
        self.rect=self.image.get_rect()
        
        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom=self.screen_react.midbottom
        
    def blitme(self):
            """Draw the shit at its current location"""
            self.screen.blit(self.image,self.rect) #blit means "draw" in Pygame.