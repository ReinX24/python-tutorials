# format specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :0(number) = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
# :% = percentage format

price1 = 300000.14159
price2 = -98756563.659
price3 = 1243563.34

# Using the f format specifier to round the number to a certain decimal value
# print(f'Price 1 is ${price1:.3f}')
# print(f'Price 2 is ${price2:.3f}')
# print(f'Price 3 is ${price3:.3f}')

# Each value has a reserved amount of spaces
# print(f'Price 1 is ${price1:10}')
# print(f'Price 2 is ${price2:10}')
# print(f'Price 3 is ${price3:10}')

# Padded with 0s at the start of the print statement
# print(f'Price 1 is ${price1:010}')
# print(f'Price 2 is ${price2:010}')
# print(f'Price 3 is ${price3:010}')

# Justifying values
# print(f'Price 1 is ${price1:<10}') # left justify
# print(f'Price 2 is ${price2:>10}') # right justify
# print(f'Price 3 is ${price3:^10}') # center justify

# Using the + value to show a plus before positive numbers
# print(f'Price 1 is ${price1:+}')
# print(f'Price 2 is ${price2:+}')
# print(f'Price 3 is ${price3:+}')

# We can also precede our print statements with just spaces
# print(f'Price 1 is ${price1: }')
# print(f'Price 2 is ${price2: }')
# print(f'Price 3 is ${price3: }')

# Using commas or underscores to represent numbers in thousands
# print(f'Price 1 is ${price1:,}')
# print(f'Price 2 is ${price2:_}')
# print(f'Price 3 is ${price3:_}')

# Mixing the different format specifiers together
print(f'Price 1 is ${price1:+,.2f}')
# ^ preceded by a + sign in positive
# add commas for thousands and round off by 2 decimal places
print(f'Price 2 is ${price2:+}')
print(f'Price 3 is %.2f' % price3)  # using the % format specifier to print variables
