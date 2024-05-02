import pygame.font


class Scoreboard:
    """A class to report scores"""

    def __init__(self, sg_game):
        self.screen = sg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sg_game.settings
        self.stats = sg_game.stats

        #font settings for scoring information

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare the score image
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #display the socre in the top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw the score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)