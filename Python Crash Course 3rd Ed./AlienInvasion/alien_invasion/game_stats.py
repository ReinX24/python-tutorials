class GameStats:
	"""Track statistics for Alien Invasion."""

	def __init__(self, ai_game):
		"""Initialize the statistics."""
		self.settings = ai_game.settings
		self.reset_stats()

		# High score should never be reset.
		self.high_score = 0

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.settings.ship_limit
		# Counts number of misses for target practice (14 - 3)
		# self.num_misses = 0
		self.score = 0
