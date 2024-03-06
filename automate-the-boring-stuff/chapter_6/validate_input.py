while True:
    print("Enter your age:")
    age = input()
    if age.isdecimal():
        # Checks if the input consists of and numbers and is not blank
        break
    print("Please enter a number for your age.")

while True:
    print("Select a new password (letters and numbers only):")
    password = input()
    if password.isalnum():
        # Checks if the input consists of letters and numbers and is not blank
        break
    print("Passwords can only have letters and numbers.")
