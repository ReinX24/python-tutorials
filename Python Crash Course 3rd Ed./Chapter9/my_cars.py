# Importing 2 classes from the car class
# from car import Car, ElectricCar

# Importing an entire module
import car

# Creating class instances using the module itself
my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# Creating class instances using imported classes
# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
