from pathlib import Path  # importing the Path class to our module

# import os

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()  # this splits each line into a list with elements
for line in lines:
	print(line)

# path = Path('pi_digits.txt')  # storing the path of our file
# contents = path.read_text().rstrip()  # storing the text content of the file
# contents = contents.rstrip()  # removing whitespace at the right of the string
# print(contents)

# Using a relative path to find our text file
# relative_path = Path('python_work/text_files/filename.txt')
# contents = relative_path.read_text()
# print(contents)

# Using an absolute path to find our text file
# absolute_path = Path(os.path.abspath(relative_path))
# contents = absolute_path.read_text()
# print(contents)
