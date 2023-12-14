import sys
from random import randint
from time import sleep

import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
# from character import Character
from bullet import Bullet
from alien import Alien


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

		# Create an instance to store game statistics.
		self.stats = GameStats(self)

		# Setting screen size with settings instance
		self.screen = pygame.display.set_mode((self.settings.screen_width,
											   self.settings.screen_height))

		# Making the screen size full screen take up the entire screen.
		# self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height

		# Creating an instance of a ship and pass in the attributes of the game.
		self.ship = Ship(self)

		# Creating a group that will hold our bullets.
		self.bullets = pygame.sprite.Group()

		# Creating a group that will hold our aliens.
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

	# Creating an instance of a character to be added to the middle.
	# self.character = Character(self)

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_aliens()

			# Printing the amount of bullets on screen to our console.
			# print(len(self.bullets))

			# Make the game run at 60 frames per second, runs for loop 60 times
			# per second.
			self._update_screen()
			self.clock.tick(60)

	def _check_events(self):
		"""Respond to key presses and mouse events."""
		# Watch for keyboard and mouse events.
		for event in pygame.event.get():
			# If the user clicks on the close button, exit the game.
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Helper method for responding to key presses."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		"""Helper method for responding to key releases."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		elif event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False

	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group."""
		if len(self.bullets) < self.settings.bullets_allowed:
			# Only create a maximum of 3 bullets.
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Update the position of bullets and get rid of old bullets."""
		# Update bullet positions.
		self.bullets.update()

		# Get rid of bullets that have disappeared.
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

		self._check_bullet_alien_collisions()

	def _check_bullet_alien_collisions(self):
		"""Respond to bullet-alien collisions."""
		# Remove any bullets and aliens that have collided.
		# Check for any bullets that have hit aliens.
		#   If so, get rid of the bullet and the alien.
		# This returns a key value pair stored in a dictionary that stores
		# the bullet and the alien that has collided and deletes them (true,
		# true).
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
												True, True)

		# Check if there are any aliens left.
		if not self.aliens:
			# Destroy existing bullets and create new fleet.
			self.bullets.empty()
			self._create_fleet()
		random_x = randint(-10, 10)

	def _update_aliens(self):
		"""
		Check if the fleet is at an edge, then update positions.
		Update the positions of all aliens in the fleet.
		"""
		self._check_fleet_edges()
		self.aliens.update()

		# Look for alien-ship collisions.
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self.ship_hit()

	def ship_hit(self):
		"""Respond to the ship being hit by an alien."""
		# Decrement ships_left
		self.stats.ships_left -= 1

		# Get rid of any remaining bullets and aliens.
		self.bullets.empty()
		self.aliens.empty()

		# Create a new fleet and center the ship.
		self._create_fleet()
		self.ship.center_ship()

		# Pause the game for .5 seconds
		sleep(0.5)

	def _create_fleet(self):
		"""Create the fleet of aliens."""
		# Create an alien and keep adding aliens until there is no room left.
		# Spacing between aliens is one alien width.
		alien = Alien(self)
		# alien_width = alien.rect.width
		alien_width, alien_height = alien.rect.size  # returns a tuple

		current_x, current_y = alien_width, alien_height
		while current_y < (self.settings.screen_height - 3 * alien_height):
			while current_x < (self.settings.screen_width - 2 * alien_width):
				self._create_alien(current_x, current_y)

				# Randomize the positions of ships (13 - 5)
				# random_x = randint(alien_width, self.settings.screen_width - 2
				# 				   * alien_width)
				# random_y = randint(alien_height, self.settings.screen_height -
				# 				   3 * alien_height)
				# self._create_alien(random_x, random_y)

				current_x += 2 * alien_width

			# Finished a row; reset x value and increment y value.
			current_x = alien_width
			current_y += 2 * alien_height

	# Place the stars at random locations (13 - 2)
	# star_amount = 0
	# while star_amount < 45:
	# 	random_x = randint(alien_width, self.settings.screen_width)
	# 	random_y = randint(alien_height, self.settings.screen_height)
	# 	self._create_alien(random_x, random_y)
	# 	star_amount += 1

	def _create_alien(self, x_position, y_position):
		"""Create an alien and place it in the fleet."""
		new_alien = Alien(self)

		new_alien.x = x_position
		new_alien.rect.x = x_position

		new_alien.y = y_position
		new_alien.rect.y = y_position

		self.aliens.add(new_alien)

	def _check_fleet_edges(self):
		"""Respond appropriately if any aliens have reached an edge."""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	# Check if we need to make a new row of raindrops (13 - 4)
	# make_new_row = False
	# for alien in self.aliens.copy():
	#     if alien.check_edges():
	#         self.aliens.remove(alien)
	#         make_new_row = True

	# if make_new_row:
	#     # Create a new row of aliens at the top (13 - 4).
	#     alien = Alien(self)
	#     # alien_width = alien.rect.width
	#     alien_width, alien_height = alien.rect.size  # returns a tuple
	#
	#     current_x = alien_width
	#     current_y = -1 * alien_height
	#     while current_x < (
	#             self.settings.screen_width - 2 * alien_width):
	#         self._create_alien(current_x, current_y)
	#         current_x += 2 * alien_width

	def _change_fleet_direction(self):
		"""Drop the entire fleet and change the fleet's direction."""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed

		# Drop towards the left (13 - 5)
		# alien.rect.x -= self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _check_aliens_bottom(self):
		"""Check if any aliens have reached the bottom of the screen."""
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= self.settings.screen_height:
				# Treat this the same as if the ship got hit.
				self._ship_hit()
				break

	def _update_screen(self):
		"""Update images on the sceen, and flip to the new screen."""
		# Redraw the screen during each pass through the loop.
		self.screen.fill(self.settings.bg_color)

		# Shoot the bullets on our screen.
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		# Draw the ship to our screen
		self.ship.blitme()

		# Draw the alien/s to our sceen.
		self.aliens.draw(self.screen)

		# Draw the character to our screen
		# self.character.blitme()

		# Make the most recently drawn screen visible.
		pygame.display.flip()


if __name__ == '__main__':
	# Make a game instance, and run the game.
	# This only runs if the file is called directly.
	ai = AlienInvasion()
	ai.run_game()
