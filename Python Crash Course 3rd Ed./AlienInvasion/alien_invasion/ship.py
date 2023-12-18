import pygame


class Ship:
	"""A class to manage the ship."""

	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the ship image and get its rect.
		# self.image = pygame.image.load('../images/ship.bmp')
		self.image = pygame.image.load('../images/ship-sideway.bmp')
		self.rect = self.image.get_rect()

		# Start each new ship at the bottom center of the screen.
		# self.rect.midbottom = self.screen_rect.midbottom

		# Start at the middle of the screen. (12 - 4)
		# self.rect.center = self.screen_rect.center

		# Start on the left side of the screen (12 - 6)
		self.rect.midleft = self.screen_rect.midleft

		# Start a float for the ship's exact horizontal position.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Movement flag; start with a ship that's not moving.
		self.moving_right = False
		self.moving_left = False

		# Movement flags for moving the ship up and down. (12 - 4)
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update the ship's position based on the movement flag."""
		if (self.moving_right and self.rect.x < self.screen_rect.right -
				self.rect.width):
			# self.rect.x += 1
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.x > 0:
			# self.rect.x -= 1
			self.x -= self.settings.ship_speed
		if self.moving_up and self.rect.y > 0:
			self.y -= self.settings.ship_speed
		if (self.moving_down and self.rect.y < self.screen_rect.height -
				self.rect.height):
			self.y += self.settings.ship_speed

		# Update the rect object from self.x
		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""Center the ship on the screen."""
		# self.rect.midbottom = self.screen_rect.midbottom
		self.rect.midleft = self.screen_rect.midleft
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
