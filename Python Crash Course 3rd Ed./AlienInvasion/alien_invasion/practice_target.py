import pygame


class Target:
	"""Class for creating a rectangular object to be used as target practice."""

	def __init__(self, ai_game):
		"""Create a rectangle at the center of the left side of the screen."""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		self.settings = ai_game.settings
		self.color = self.settings.target_color

		# Set the dimensions and properties of the target.
		self.width = self.settings.target_width
		self.height = self.settings.target_height

		# Build the rectangle and center it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.center_target()

		# Setting the direction of the target
		self.direction = 1

	def update(self):
		"""Move the ship up and down."""
		self.y += self.direction * self.settings.target_speed

		if self.rect.top < 0:
			self.rect.top = 0
			self.direction = 1
		elif self.rect.bottom > self.screen_rect.bottom:
			self.rect.bottom = self.screen_rect.bottom
			self.direction = -1

		self.rect.y = self.y

	def center_target(self):
		"""Center the target on the right side of the screen."""
		self.rect.midright = self.screen_rect.midright
		self.y = float(self.rect.y)  # makes movement smoother

	def draw_target(self):
		"""Draw the target to our screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)
