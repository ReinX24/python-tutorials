import sys

import pygame

from settings import Settings

from ship import Ship

from character import Character


class AlienInvasion:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game, and create game resources."""
		pygame.init()

		# self.screen = pygame.display.set_mode((1200, 800))  # screen size
		# self.bg_color = (230, 230, 230)  # light gray background

		pygame.display.set_caption("Alien Invasion")  # window title

		self.clock = pygame.time.Clock()  # creating a Clock instance for frames

		self.settings = Settings()

		# Setting screen size with settings instance
		self.screen = pygame.display.set_mode((self.settings.screen_width,
											   self.settings.screen_height))

		# Creating an instance of a ship and pass in the attributes of the game.
		self.ship = Ship(self)

		# Creating an instance of a character
		self.character = Character(self)

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()
			self._update_screen()
			self.ship.update()
			# Make the game run at 60 frames per second, runs for loop 60 times
			# per second.
			self.clock.tick(60)

	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		# Watch for keyboard and mouse events.
		for event in pygame.event.get():
			# If the user clicks on the close button, exit the game.
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					# Checking if the pressed key is the right arrow.
					self.ship.moving_right = True
				elif event.key == pygame.K_LEFT:
					self.ship.moving_left = True

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					# Checking if the key that is let go is right arrow.
					self.ship.moving_right = False
				elif event.key == pygame.K_LEFT:
					self.ship.moving_left = False

	def _update_screen(self):
		"""Update images on the sceen, and flip to the new screen."""
		# Redraw the screen during each pass through the loop.
		self.screen.fill(self.settings.bg_color)

		# Draw the ship to our screen
		self.ship.blitme()

		# Draw the character to our screen
		self.character.blitme()

		# Make the most recently drawn screen visible.
		pygame.display.flip()


if __name__ == '__main__':
	# Make a game instance, and run the game.
	# This only runs if the file is called directly.
	ai = AlienInvasion()
	ai.run_game()
