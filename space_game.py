import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class SpaceGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Intialize the game and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Space Game")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        #set the background colour
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            #get rid of bullets that have gone off the screen
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))
            self._update_screen()
            self.clock.tick(120)

    def _check_events(self):
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_d:
            # Move the ship to the right
            self.ship.rect.x += 5
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.rect.x -= 5
            self.ship.moving_left = True
        elif event.key == pygame.K_w:
            self.ship.rect.y -= 5
            self.ship.moving_up = True
        elif event.key == pygame.K_s:
            self.ship.rect.y += 5
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    def _check_keyup_events(self, event):
        """respond to key releases"""
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        if event.key == pygame.K_a:
            self.ship.moving_left = False
        if event.key == pygame.K_w:
            self.ship.moving_up = False
        if event.key == pygame.K_s:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        # Redraw the screen every loop
        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        # Make the most recently drawn screen visable
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game
    sg = SpaceGame()
    sg.run_game()
