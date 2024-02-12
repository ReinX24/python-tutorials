print(
    """Hello, World
What is your name?"""
)

myName = input()

print(
    f"""It is good to meet you, {myName}
The length of your name is: 
{len(myName)}
What is your age?"""
)

myAge = input()

print(f"You will be {int(myAge) + 1} in a year.")
