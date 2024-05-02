class Settings:
    """A class to save all the settings for Space Game"""

    def __init__(self):
        """Initialize the games settings"""
        # Screen settings
        self.screen_width = 1400
        self.screen_height = 1000
        self.bg_color = (0, 0, 230)

        # Ship settings
        self.ship_speed = 5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 20.0
        self.bullet_width = 6
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet dir of 1 represenets right, -1 represents left
        self.fleet_direction = 1
