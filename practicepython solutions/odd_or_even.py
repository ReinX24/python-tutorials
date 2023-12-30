def main():
    number = int(input('Enter a number: '))
    print(check_odd_or_even(number))
    num, check = int(input('Enter num: ')), int(input('Enter check: '))
    print(check_divides_evenly(num, check))

def check_odd_or_even(number):
    if number % 4 == 0:
        return "Multiple of 4"
    elif number % 2 == 0:
        return "Even" 
    else:
        return "Odd"

def check_divides_evenly(num, check):
    return f'{num} divides evenly by {check}' if num % check == 0 else f'{num} does not divide evenly by {check}'

if __name__ == '__main__':
    main()