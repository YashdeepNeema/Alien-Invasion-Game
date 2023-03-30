import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Overall class to manage game and behaviour."""

    def __init__(self):
        """Initialize the game and, create game resources."""

        pygame.init()  #initialize the pygame module.
        self.settings = Settings()

        # To create a display window
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # To set the background color:
        #self.bg_color = self.settings.bg_color

    def run_game(self):
        """Start the main lop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # to make screen visible
            pygame.display.flip()

            # to redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

if __name__ == "__main__":
    # Make a game instance, and run the game:
    ai = AlienInvasion()
    ai.run_game()