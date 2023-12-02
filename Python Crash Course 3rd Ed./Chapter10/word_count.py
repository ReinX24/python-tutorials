from pathlib import Path


def count_words(path):
	"""Count the approximate number of words in a file."""
	missing_files_path = Path('missing_files.txt')
	missing_files = missing_files_path.read_text()
	try:
		contents = path.read_text(encoding='utf-8')
	except FileNotFoundError:
		# print(f"Sorry, the file {path} does not exist.")
		# Using the pass keyword so that the except block does not do anything
		# pass
		missing_files += f"{path}\n"
		missing_files_path.write_text(missing_files)
	else:
		# Count the approximate words in the text file:
		words = contents.split()
		word_count = len(words)
		print(f"The file {path} has about {word_count:,} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt',
			 'norwegian_wood.txt']
for filename in filenames:
	path = Path(filename)
	count_words(path)
