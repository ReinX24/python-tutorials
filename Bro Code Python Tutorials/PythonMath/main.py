import math
# my_friends = 10
# my_friends = my_friends + 1
# my_friends += 1

# my_friends = my_friends - 2
# my_friends -= 2

# my_friends = my_friends * 3
# my_friends *= 3

# my_friends = my_friends / 2
# my_friends /= 2

# my_friends = my_friends ** 2
# my_friends **= 2

# remainder = my_friends % 3
# remainder = my_friends % 2

# print(remainder)

# x = 3.14
# y = -4
# z = 5

# Rounding a number to the nearest whole integer round()
# result = round(x)

# Absolute value of a number abs()
# result = abs(y)

# Power of a number pow(base, exponent)
# result = pow(4, 3)

# Max value within numbers max()
# result = max(x, y, z)

# Min value within numbers min()
# result = min(x, y, z)

# print(result)

# Different math constants
# print(math.pi)
# print(math.e)
# result = math.sqrt(9)
# result = math.ceil(9.1)
# result = math.floor(9.9)

# print(result)

# Calculate the circumference of a circle
# radius_input = float(input("Enter the radius of a circle: "))
# circumference_result = 2 * math.pi * radius_input
# print(f"The circumference of the circle is {round(circumference_result, 2)}cm")

# Calculate the area of a circle
# radius_input = float(input("Enter the radius of a circle: "))
# area_result = math.pi * pow(radius_input, 2)
# print(f"The area of the circle is {round(area_result, 2)}cm^2")

# Finding the hypotenuse of a right triangle
a_side = float(input("Enter side A: "))
b_side = float(input("Enter side b: "))

c_side = math.sqrt(pow(a_side, 2) + pow(b_side, 2))

print(f"Side C = {c_side}")
