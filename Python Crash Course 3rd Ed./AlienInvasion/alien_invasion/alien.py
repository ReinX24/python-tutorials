import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('../images/alien.bmp')

        # Replacing aliens with stars (13 - 1)
        # self.image = pygame.image.load('../images/star.bmp')

        # Replacing the aliens with raindrops (13 - 3)
        # self.image = pygame.image.load('../images/raindrop.bmp')

        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

        # Store the alien's y-axis
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

        # Check if any of the fleet hits the ground. (13 - 3).
        # Also check if any of the fleet hits the ceiling (13 - 5).
        # return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)

        # Check if any ships has hit the top or bottom of the screen.
        # return (self.rect.top >= screen_rect.top) or (self.rect.bottom >=
        #                                  screen_rect.bottom)

    def update(self):
        """Move the alien to the right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

        # Making the raindrop just move down (13 - 3)
        # self.rect.y += self.settings.fleet_direction

        # Make the fleet move up and down instead of sideways (13 - 5).
        # self.y += self.settings.alien_speed * self.settings.fleet_direction
        # self.rect.y = self.y
