import sys
import pygame
from time import sleep

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button

class SpaceGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Intialize the game and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Space Game")

        #Create an isntance to store game stats
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        #set the background colour
        self.bg_color = (self.settings.bg_color)

        #start the game in an inactive state
        self.game_active = False

        #make the difficulty buttons
        self.easy_button = Button(self, "Easy", -200)
        self.standard_button = Button(self, "Standard")
        self.hard_button = Button(self, "Hard", 200)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_easy_button(mouse_pos)
                self._check_standard_button(mouse_pos)
                self._check_hard_button(mouse_pos)

    def _check_easy_button(self, mouse_pos):
        """start a new game when player clicks easy"""
        button_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.speed_multiplier = 1
            self._start_game()

    def _check_standard_button(self, mouse_pos):
        """start a new game when player clicks easy"""
        button_clicked = self.standard_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.speed_multiplier = 1.25
            self._start_game()

    def _check_hard_button(self, mouse_pos):
        """start a new game when player clicks easy"""
        button_clicked = self.hard_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.speed_multiplier = 1.5
            self._start_game()

    def _start_game(self):
        """reset stats and start a new game"""
        self.settings.init_dynamic_settings(self.speed_multiplier)
        pygame.mouse.set_visible(False)
        self.stats.reset_stats()
        self.game_active = True
        self.bullets.empty()
        self.aliens.empty()
        self._create_fleet()
        self.ship.centre_ship()


    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_d:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_w:
            self.ship.moving_up = True
        elif event.key == pygame.K_s:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()

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
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        # get rid of bullets that have gone off the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        #check for bullets that have hit aliens
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _create_alien(self, position_x, position_y):
        """create an alien and place it in the row"""
        new_alien = Alien(self)
        new_alien.x = position_x
        new_alien.rect.x = position_x
        new_alien.rect.y = position_y
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond if fleets meets an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_fleet(self):
        """Create the fleet of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 5 * alien_height):

            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 1.5 * alien_height

    def _update_aliens(self):
        """Update positions of the aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        #look for alien ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #look for aliens at the bottom of the screen
        self._check_aliens_bottom_screen()

    def _ship_hit(self):
        """Respond to ship being hit by alien"""
        if self.stats.ships_left > 0:
            #Decrement ships left
            self.stats.ships_left -= 1

            #remove remaining bullets and aliens
            self.aliens.empty()
            self.bullets.empty()

            #create new fleet and ship
            self._create_fleet()
            self.ship.centre_ship()

            #ppause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom_screen(self):
        """check for aliens at the bottomw of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _update_screen(self):
        # Redraw the screen every loop
        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        if not self.game_active:
            self.easy_button.draw_button()
            self.standard_button.draw_button()
            self.hard_button.draw_button()

        # Make the most recently drawn screen visable
        pygame.display.flip()



if __name__ == "__main__":
    # Make a game instance, and run the game
    sg = SpaceGame()
    sg.run_game()
