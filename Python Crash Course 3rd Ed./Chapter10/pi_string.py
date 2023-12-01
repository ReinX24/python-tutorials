import math
from pathlib import Path

# path = Path('pi_digits.txt')
path = Path('pi_million_digits.txt')  # printing the 1,000,000 digits of pi
# after the 3.
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
	pi_string += line.lstrip()

# print(pi_string)
print(f"{pi_string[:52]}...")
print(len(pi_string))
