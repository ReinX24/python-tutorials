import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):  # inheriting Sprite class attributes from pygame.
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)

        # Bullets start at the midtop of the ship instance.
        self.rect.midtop = ai_game.ship.rect.midtop

        # Bullets start at mid left of the ship.
        # self.rect.midleft = ai_game.ship.rect.midleft

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)

        # Store the bullet's position in the x-axis. (12 - 6)
        # self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen."""

        # Update the exact position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    # Update the position of the bullet in the x-axis. (12 - 6)
    # self.x += self.settings.bullet_speed
    # self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
