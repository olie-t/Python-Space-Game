import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, sg_game):
        """Create a bullet at the ships present position"""
        super().__init__()
        self.screen = sg_game.screen
        self.settings = sg_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet at rect (0, 0 ) and then set the correct positon.

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = sg_game.ship.rect.midtop

        # Store the bullets position as a float
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)

class AlienBullet(Sprite):
    """ A Class to manage bullets fired from the aliens"""

    def __init__(self, sg_game, alien):
        super().__init__()
        self.screen = sg_game.screen
        self.settings = sg_game.settings
        self.color = self.settings.alien_bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midtop = alien.rect.midbottom
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.alien_bullet_speed
        self.rect.y = self.y

    def draw_alien_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)



