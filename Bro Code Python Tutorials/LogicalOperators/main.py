# logical operators = used on conditional statements
# and = checks if two or more conditions are True
# or = checks if at least one condition is True
# not = True if condition is False, and vice versa
# Checks if the temp is greater than 0 AND less than 30
temp = 20
sunny = False
if temp <= 0 or temp >= 30:
    print('The temperature is bad')
else:
    print('The temperature is good')

# not inverts the sunny boolean value
# prints if sunny is False since it will be converted to True
if not sunny:
    print('It is cloudy outside!')
else:
    print('It is sunny!')
