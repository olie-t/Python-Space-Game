class Settings:
    """A class to save all the settings for Space Game"""

    def __init__(self):
        """Initialize the games settings"""
        # Screen settings
        self.screen_width = 1400
        self.screen_height = 1000
        self.bg_color = (0, 0, 230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)