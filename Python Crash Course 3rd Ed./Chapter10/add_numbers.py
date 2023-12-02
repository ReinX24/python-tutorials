print("[Addition Calculator]")
print("Enter 'q' to quit.")

while True:
	try:
		first_number = input("\nEnter first number: ")
		if first_number == 'q':
			break
		second_number = input("Enter second number: ")
		if second_number == 'q':
			break
		sum_number = int(first_number) + int(second_number)
	except ValueError:
		print("\nInvalid input! Please enter a number.")
	else:
		print(
			f"\nThe sum of {first_number} and {second_number} is {sum_number}.")
