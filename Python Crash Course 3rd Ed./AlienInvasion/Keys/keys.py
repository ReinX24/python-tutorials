import os
import sys

import pygame

from alien_invasion import settings


class Keys:
	"""Creating a window and tracks key movements."""

	def __init__(self):
		"""Overall class to keep track of key presses."""
		pygame.display.set_caption("Keys 12 - 5")

		self.clock = pygame.time.Clock()

		self.settings = settings.Settings()

		self.screen = pygame.display.set_mode((1200, 800))

	def run_game(self):
		"""Start the main loop of the program."""
		while True:
			self._check_update()
			self._update_screen()

			self.clock.tick(60)

	def _check_update(self):
		"""Checks the key presses of the user"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
				else:
					print(event.key)

	def _update_screen(self):
		"""Update the images on the screen."""
		self.screen.fill(self.settings.bg_color)

		pygame.display.flip()


if __name__ == '__main__':
	Keys().run_game()
