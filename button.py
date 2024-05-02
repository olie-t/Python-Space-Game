import pygame.font

class Button:
    """A class to build buttons for the game"""

    def __init__(self, sg_game, message, pos_x_offset=0):
        """init button attributes"""
        self.screen = sg_game.screen
        self.screen_rect = self.screen.get_rect()

        #set the properties of the button
        self.width, self.height = 200, 50
        self.button_colour = (0, 135, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #build the buttons rect object and centre it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = ((self.screen_rect.center[0] + pos_x_offset), self.screen_rect.center[1])

        self._prep_msg(message)

    def _prep_msg(self, msg):
        """turn msg into a redered img and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_colour, self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """draw a blank button and the draw message"""
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
