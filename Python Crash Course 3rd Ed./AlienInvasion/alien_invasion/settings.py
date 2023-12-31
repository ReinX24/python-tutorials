class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		# self.bg_color = (0, 102, 153)  # blue background

		# Ship settings
		# self.ship_speed = 2.5
		self.ship_limit = 3

		# Bullet settings
		# self.bullet_speed = 2.5
		self.bullet_width = 300
		self.bullet_height = 15

		# Making the bullet into a horizontal rectangle. (12 - 6)
		# self.bullet_width = 15
		# self.bullet_height = 3

		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		# Alien settings
		# self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		# fleet direction of 1 represents right; -1 represents left.
		# self.fleet_direction = 1

		# Target settings  (14 - 2)
		self.target_width = 15
		self.target_height = 120
		self.target_color = (180, 60, 10)

		self.miss_limit = 3

		# How quickly the game speeds up
		self.speedup_scale = 1.1

		# How quickly the alien point values increase
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""
		Initialize settings that can change throughout the game.
		This will be regarded as the normal mode.
		"""
		self.ship_speed = 1.5
		self.bullet_speed = 2.5
		self.alien_speed = 1.0

		# Fleet direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		# Reset target speed (14 - 3)
		# self.target_speed = 1.5

		# Score settings
		self.alien_points = 50

	def initialize_easy_settings(self):
		"""When the user chooses easy."""
		self.ship_speed = 2
		self.bullet_speed = 4
		self.alien_speed = 0.5

		self.fleet_direction = 1

		self.alien_points = 30

	def initialize_hard_settings(self):
		"""When the user chooses hard."""
		self.ship_speed = 4
		self.bullet_speed = 8
		self.alien_speed = 1.5

		self.fleet_direction = 1

		self.alien_points = 70

	def increase_speed(self):
		"""Increase speed settings."""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		# self.target_speed *= self.speedup_scale

		# Increases the amount of points that each alien is worth as the game
		# goes faster.
		self.alien_points = int(self.alien_points * self.score_scale)
		# print(self.alien_points)
