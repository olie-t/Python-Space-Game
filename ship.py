import pygame


class Ship:
    """A class to manage to the ship"""

    def __init__(self, sg_game):
        """Init the ship and its starting position"""
        self.screen = sg_game.screen
        self.screen_rect = sg_game.screen.get_rect()
        self.settings = sg_game.settings

        # Load the ship and get its rect.
        self.image = pygame.image.load('images/green_ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ships exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag, start with a ship that,s not moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update ships position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)