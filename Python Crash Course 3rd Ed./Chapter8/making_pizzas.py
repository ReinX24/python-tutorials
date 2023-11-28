# import pizza  # importing a module
from pizza import make_pizza  # importing only a specific function
from pizza import make_pizza as mp  # importing a method with a different name
import pizza as p  # importing module with an alias

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
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
