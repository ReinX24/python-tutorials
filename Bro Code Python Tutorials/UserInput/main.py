# userName = input("Enter your name: ")
# userAge = float(input("Enter your age: "))
# userAge = userAge + 1
#
# print(f"Hello {userName}")
# print(f"You are {userAge} years old")

# Mad libs
# adjective_one = input("Enter an adjective: ")
# noun_input = input("Enter a noun: ")
# adjective_two = input("Enter an adjective: ")
# verb_input = input("Enter a verb: ")
# adjective_three = input("Enter an adjective: ")

# print(f"Today I went to a {adjective_one} zoo.")
# print(f"In an exhibit, I saw {noun_input}")
# print(f"{noun_input} was {adjective_two} and {verb_input}ing")
# print(f"I was {adjective_three}")

# Area Calc
# Typecasting input to a float
# rect_length = float(input("Enter the length of a rectangle: "))
# rect_width = float(input("Enter the width of a rectangle: "))
# rect_height = float(input("Enter the height of a rectangle: "))
# Calculating the area of our rectangle
# rect_volume = rect_length * rect_width * rect_height

# print(f"The volume is: {rect_volume}cm^3")

# Shopping Cart
ordered_item = input("What item would you like to buy?: ")
item_price = float(input("What is the price?: "))
item_quantity = int(input("How many would you like?: "))

total_price = item_price * item_quantity

print(f"""
    You have bought {item_quantity} * {ordered_item}/s    
    Your total is: ${round(total_price, 2)}""")

# round(variable, round off amount), in the example above
# it rounds the number to 2 decimal places
