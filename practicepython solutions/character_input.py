def main():
    """Main method for our program"""
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    repeat_count = int(input('Enter repeat count: '))
    repeat_result = repeat_message(tell_when__100_years_old(name, age), repeat_count)
    print(repeat_result)

def tell_when__100_years_old(name, age):
    """Tells the user when they will turn 100 years old."""
    current_year = 2023
    remaining_years = 100 - age
    return f"{name.title()} will be 100 at {current_year + remaining_years}."

def repeat_message(message, repeat_times):
    message_result = ''
    for i in range(repeat_times - 1):
        message_result += message + '\n'
    return message_result + message

if __name__ == '__main__':
    main()