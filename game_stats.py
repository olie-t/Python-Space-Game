class GameStats:
    """Track stats for the game"""

    def __init__(self, sg_game):
        self.settings = sg_game.settings
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
