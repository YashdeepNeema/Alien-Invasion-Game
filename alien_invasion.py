import sys
import pygame

class AlienInvasion:
    """Overall class to manage game and behaviour."""

    def __init__(self):
        """Initialize the game and, create game resources."""

        pygame.init()  #initialize the pygame module.

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main lop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # to make screen visible
            pygame.display.flip()

if __name__ == "__main__":
    # Make a game instance, and run the game:
    ai = AlienInvasion()
    ai.run_game()