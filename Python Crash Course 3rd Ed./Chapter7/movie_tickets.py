# active = True
#
# prompt = "\nEnter your age:"
# prompt += "\n(Enter 'quit' to exit program) "
#
# Using a flag to terminate the program
# while active:
#     age = input(prompt)
#     if age == "quit":
#         active = False
#     else:
#         age = int(age)
#         if age < 3:
#             print("Your ticket is free!")
#         elif age <= 12:
#             print("Your ticket is $10")
#         elif age > 12:
#             print("Your ticket is $15")

# Another version of the program that uses a break statement to terminate itself
prompt = "\nEnter your age:"
prompt += "\n(Enter 'quit' to exit program) "

while True:
	age = input(prompt)
	if age == "quit":
		break
	else:
		age = int(age)
		if age < 3:
			print("Your ticket is free!")
		elif age <= 12:
			print("Your ticket is $10")
		elif age > 12:
			print("Your ticket is $15")
