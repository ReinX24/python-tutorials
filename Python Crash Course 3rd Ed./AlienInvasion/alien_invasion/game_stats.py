import os


class GameStats:
	"""Track statistics for Alien Invasion."""

	def __init__(self, ai_game):
		"""Initialize the statistics."""
		self.settings = ai_game.settings
		self.reset_stats()

		self.high_score = 0

		self.read_recorded_high_score()

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.settings.ship_limit
		# Counts number of misses for target practice (14 - 3)
		# self.num_misses = 0
		self.score = 0
		self.level = 1

	def read_recorded_high_score(self):
		"""Check for a file where the current high score is writter."""
		# High score should never be reset.
		# 14 - 5 All-Time High Score
		high_score_file = "high_score.txt"
		if os.path.exists(high_score_file):
			saved_file = open(high_score_file, "r")
			recorded_high_score = int(saved_file.read())
			self.high_score = recorded_high_score
		else:
			with open(high_score_file, "w") as create_file:
				create_file.write(str(self.high_score))

	def write_new_high_score(self):
		"""Write the new high score to our file"""
		# 14 - 5 All-Time High Score
		high_score_file = "high_score.txt"
		if os.path.exists(high_score_file):
			saved_file = open(high_score_file, "w")
			saved_file.write(str(self.high_score))
