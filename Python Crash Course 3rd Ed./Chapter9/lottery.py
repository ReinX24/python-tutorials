from random import choices

numbers = (1, 3, 5, 7, 9, 11, 13, 15)
letters = ('a', 'b', 'c', 'd', 'e')

my_ticket = [1, 3, 5, 7, 'a', 'b', 'c', 'd']

check_count = 0

# While loop that keeps generating random results until it matches our ticket
while True:
	random_result = choices(numbers, k=4)
	random_result += choices(letters, k=4)
	check_count += 1
	if random_result == my_ticket:
		break
	else:
		print(check_count)

print('\nMatch found!')
print(f"My ticket: {my_ticket}")
print(f"Random ticket: {random_result}")
