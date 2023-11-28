# Counting numbers 1 to 5 using a while loop
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# Counting numbers from 1 to 10 but only prints the odd numbers
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue  # restarts the loop without executing the code block below

	print(
		current_number)  # prints current_number if the continue command is not executed
