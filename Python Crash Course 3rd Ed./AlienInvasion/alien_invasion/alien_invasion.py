import sys

import pygame


class AlienInvasion:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game, and create game resources."""
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 800))  # screen size

		pygame.display.set_caption("Alien Invasion")  # window title

		self.clock = pygame.time.Clock()  # creating a Clock instance for frames

		self.bg_color = (230, 230, 230)  # light gray background

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			# Watch for keyboard and mouse events.
			for event in pygame.event.get():
				# If the user clicks on the close button, exit the game.
				if event.type == pygame.QUIT:
					sys.exit()

			# Redraw the screen during each pass through the loop.
			self.screen.fill(self.bg_color)

			# Make the most recently drawn screen visible.
			pygame.display.flip()

			# Make the game run at 60 frames per second, runs for loop 60 times
			# per second.
			self.clock.tick(60)


if __name__ == '__main__':
	# Make a game instance, and run the game.
	# This only runs if the file is called directly.
	ai = AlienInvasion()
	ai.run_game()
