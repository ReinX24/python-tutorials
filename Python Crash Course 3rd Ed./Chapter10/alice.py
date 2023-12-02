from pathlib import Path

path = Path('alice.txt')
# Using utf-8 encoding just in case the system and file encoding does not match.
# This is most likely to happen when reading from a file that wasn't created
# on your system.
try:
	contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
	print(f"Sorry, the file {path} does not exist.")
else:
	# Counting the approximate amount of words in the file:
	# .split splits the text into a list elements when there is whitespace
	words = contents.split()
	num_words = len(words)
	print(f"The file {path} has about {num_words:,} words.")
