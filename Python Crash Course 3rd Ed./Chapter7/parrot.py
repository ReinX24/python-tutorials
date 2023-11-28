# message = input('Tell me something, and I will repeat it back to you: ')
# print(message)

# Making the program run until the user chooses to quit the program
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""

# Adding a flag that will store a boolean value to see if the program should keep running or not
active = True

while active:
	message = input(prompt)

	# Makes sure that when the user enters quit, it does not print 'quit' in the console
	if message == "quit":
		active = False
	else:
		print(message)
