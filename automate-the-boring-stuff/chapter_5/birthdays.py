birthdays = {"Alice": "Apr 1", "Bob": "Dec 12", "Carol": "Mar 4"}

while True:
    print("Enter a name: (blank to quit)")
    name = input()

    if name == "":
        break

    if name in birthdays:
        print(f"{birthdays[name]} is the birthday of {name}")
    else:
        print(f"I do not have birthday information for {name}")
        print("What is their birthday?")
        new_birth_date = input()
        birthdays[name] = new_birth_date  # Adds a new key value pair
        print("Birthday database updated.")
