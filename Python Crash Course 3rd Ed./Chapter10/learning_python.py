from pathlib import Path

# Finding the path in our directory
path = Path('learning_python.txt')
contents = path.read_text()

# Replacing the word 'Python' with 'C' in our string
contents = contents.replace('Python', 'C')

# Printing the contents directly
print(contents)

# Printing the contents by storing each line in a list and printing each line
# lines = contents.splitlines()
for line in contents.splitlines():
	print(line)
