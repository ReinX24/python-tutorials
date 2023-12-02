print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break

	# Catching possible ZeroDivisionError
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		# This executes when the try block does not catch any errors
		print(answer)

# Handling a ZeroDivisionError using a try-except block
# try:
# 	print(5 / 0)
# except ZeroDivisionError:
# 	print("You can't divide by zero!")
