# Importing 2 classes from the car class
# from car import Car, ElectricCar

# Importing an entire module
# import car

# Importing the car and electric car module separately
# from car import Car
# from electric_car import ElectricCar

# Importing a class with alias
# from electric_car import ElectricCar as EC

# Importing an entire module with an alias
import electric_car as ec

my_leaf = ec.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# my_leaf = EC('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# Creating class instances using the module itself
# my_mustang = car.Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())
# my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# Creating class instances using imported classes
# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
