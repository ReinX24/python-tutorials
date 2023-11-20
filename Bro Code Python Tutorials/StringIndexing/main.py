# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = '1234-5678-9012-3456'
# print(credit_number[2])  # prints a character at a certain index
# print(credit_number[0:4])  # prints first character until third character

# Print 5678
# print(credit_number[5:9])

# Print 5 all to the end of the string
# print(credit_number[5:])

# Print the last character of the string
# print(credit_number[-1])

# Printing every second character in the string, start from the first char, third char, etc.
# :: means start to end of the string
# print(credit_number[::2])
# print(credit_number[::3]) # 14...

# Get the last 4 digits in the string
last_digits = credit_number[-4:]
print(f'XXXX-XXXX-XXXX-{last_digits}')

# Prints the string in reverse
credit_number = credit_number[::-1]
print(credit_number)