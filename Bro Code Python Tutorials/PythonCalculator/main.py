operator = input('Enter an operator (+ - * /): ')
num_one = float(input('Enter the 1st number: '))
num_two = float(input('Enter the 2nd number: '))

if operator == '+':
    result = num_one + num_two
    print(f'The result is {round(result, 3)}')
elif operator == '-':
    result = num_one - num_two
    print(f'The result is {round(result, 3)}')
elif operator == '*':
    result = num_one * num_two
    print(f'The result is {round(result, 3)}')
elif operator == '/':
    result = num_one / num_two
    print(f'The result is {round(result, 3)}')
else:
    print(f'{operator} is not a valid operator')
