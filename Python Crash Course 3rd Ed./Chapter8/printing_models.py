# Importing functions from printing_functions module
# import printing_functions
# import printing_functions as pf

# Importing functions directly
# from printing_functions import *
# from printing_functions import print_models
# from printing_functions import show_completed_models
from printing_functions import print_models as pm
from printing_functions import show_completed_models as scd

# Using our imported module and its functions
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm(unprinted_designs, completed_models)
scd(completed_models)

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# printing_functions.print_models(unprinted_designs, completed_models)
# printing_functions.show_completed_models(completed_models)

# pf.print_models(unprinted_designs, completed_models)
# pf.show_completed_models(completed_models)

# Using while loops to loop through our list
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)
#
# print("\nThe following models have been completed:")
# for completed_model in completed_models:
#     print(completed_model)

# Using functions to loop through our list
# def print_models(unprinted_designs, completed_models):
#     """
#     Simulate printing each design, until none are left.
#     Move each design to completed_models after printing.
#     """
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)


# def show_completed_models(completed_models):
"""Show all the models that were printed."""
# print(f"\nThe following models have been printed: ")
# for completed_model in completed_models:
#     print(completed_model)


# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)  # this affects the original lists
# show_completed_models(completed_models)

# Instead of modifying the original list, we will instead only pass in a copy of it
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# Passing in a copy of unprinted_designs list
# print_models(unprinted_designs[:], completed_models)  # this affects the original lists
# show_completed_models(completed_models)

# Checking of the original list is unaffected
# print(unprinted_designs)
# print(completed_models)
