# typecasting = The process of converting a value of one data type to another
#               (string, integer, float, boolean)
#               Explicit vs Implicit

person_name = "Rein"
person_age = 20
grade_average = 91.1
is_student = True

# Explicit type casting

# Printing the types of our variables
# print(type(person_name))
# print(type(person_age))
# print(type(grade_average))
# print(type(is_student))

# Converting integer to float
# print(type(person_age))
# person_age = float(person_age)
# print(type(person_age))

# Converting float to integer
# print(type(grade_average))
# grade_average = int(grade_average)
# print(type(grade_average))

# Converting from boolean to string
# print(type(is_student))
# is_student = str(is_student)
# print(type(is_student))

# Converting from integer to boolean
# print(type(person_age))
# Converts to true, any number other than 0 returns true
# person_age = bool(person_age)
# print(type(person_age))
# print(person_age)

# Converting string to boolean
# print(type(person_name))
# Converts to true if the string is not empty, false if the string is empty
# person_name = bool(person_name)
# print(type(person_name))
# print(person_name)

# Implicit type casting

x = 2
y = 2.0

x = x / y
# Converts result to float
print(type(x))
print(x)