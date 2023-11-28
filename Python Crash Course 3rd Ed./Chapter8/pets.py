# Using positional arguments in a function
# When using default parameters, make sure that it is at the end of the parameter list so that
# positional parameters could still work for parameters before it.
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# describe_pet("hamster", "harry")
# describe_pet("dog", "willie")
# describe_pet("harry", "hamster")

# Using keyword arguments to pass in data to function parameters
# This specifies which value is passed to which parameter within our function
# describe_pet(animal_type="hamster", pet_name="harry")
# describe_pet(pet_name="willie", animal_type="dog")

# Making use of default values in our function
# describe_pet(pet_name="willie")
# describe_pet('willie')
# describe_pet(pet_name='harry', animal_type='hamster')

# A dog named Willie.
# describe_pet(pet_name='willie')
# describe_pet('willie')

# A hamster named Harry
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')

# Calling a function without paraters
# describe_pet() # causes an exception