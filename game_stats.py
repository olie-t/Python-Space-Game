from pathlib import Path


class GameStats:
    """Track stats for the game"""

    def __init__(self, sg_game):
        self.settings = sg_game.settings
        self.reset_stats()
        #high score should never be reset
        path = Path('high_score.txt')
        if path.exists():
            self.high_score = int(path.read_text())
        else:
            self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
