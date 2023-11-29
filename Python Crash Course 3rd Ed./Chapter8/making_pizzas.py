# import pizza  # importing a module
from pizza import make_pizza  # importing only a specific function
from pizza import make_pizza as mp  # importing a method with a different name
# import pizza as p  # importing module with an alias
from pizza import *  # import all methods in pizza module

# Using the functions within a module
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using imported method/s instead of an entire module
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using method aliases
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using module aliases
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# When all the methods are imported, we can use these methods without the
# module name. This is not recommended since it may cause confusion within
# functions within the file and from external modules.
# The recommended way of importing methods is by importing them individually
# or by importing the entire module and accessing methods using the dot
# notation.
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
