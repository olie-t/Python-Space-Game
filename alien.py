import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent enemy aliens"""

    def __init__(self, sg_game):
        """Init the alien and set start position"""
        super().__init__()
        self.screen = sg_game.screen
        self.settings = sg_game.settings

        #load the alien image and set its rect
        self.image = pygame.image.load('images/smalldrone.bmp')
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the exact position for the alien
        self.x = float(self.rect.x)

    def update(self):
        """Move alien"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return true if an alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
