from random import randint


class Die:

	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		print(randint(1, self.sides))


# Creating an instance of our Die class and using the roll_die method

# 6 side dice
# die_one = Die()
# for i in range(10):
# 	die_one.roll_die()

# 10 side dice
# die_one = Die(10)
# for i in range(10):
# 	die_one.roll_die()

# 20 side die
die_one = Die(20)
for i in range(10):
	die_one.roll_die()
