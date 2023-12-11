import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
	"""A class to represent a single alien in the fleet."""

	def __init__(self, ai_game):
		"""Initialize the alien and set its starting position."""
		super().__init__()
		self.screen = ai_game.screen

		# Load the alien image and set its rect attribute.
		self.image = pygame.image.load('../images/alien.bmp')

		# Replacing aliens with stars (13 - 1)
		# self.image = pygame.image.load('../images/star.bmp')

		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the alien's exact horizontal position
		self.x = float(self.rect.x)