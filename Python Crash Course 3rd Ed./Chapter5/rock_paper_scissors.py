import random

choices = ['rock', 'paper', 'scissors']

user_choice = input('''# Choices
	[r] rock
	[p] paper
	[s] scissors
Pick your weapon: ''').lower()

computer_choice = random.choice(choices)

if user_choice == 'r':
	user_choice = 'rock'
elif user_choice == 'p':
	user_choice = 'paper'
elif user_choice == 's':
	user_choice = 'scissors'
else:
	print('[Invalid Choice]')
	exit()

print(f'''
	User: {user_choice}
	Computer: {computer_choice}
''')

if user_choice == computer_choice:
	print('Tie!')
elif user_choice == 'rock' and computer_choice == 'scissors':
	print('You win!')
elif user_choice == 'paper' and computer_choice == 'rock':
	print('You win!')
elif user_choice == 'scissors' and computer_choice == 'paper':
	print('You win!')
else:
	print('You lose!')
