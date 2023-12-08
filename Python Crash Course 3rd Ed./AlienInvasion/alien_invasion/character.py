import pygame


class Character:
	"""Creating a Character to be in the center of the screen."""

	def __init__(self, ai_game):
		"""Create an instance of the Character class."""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		self.image = pygame.image.load('../images/character.bmp')
		self.rect = self.image.get_rect()

		self.rect.center = self.screen_rect.center


	def blitme(self):
		"""Draw the ship to its current location."""
		self.screen.blit(self.image, self.rect)