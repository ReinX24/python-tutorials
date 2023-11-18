# Python weight converter
# Convert pounds (lb) to kilograms (kg) and vice versa

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == 'K':
    weight *= 2.20462
    unit = 'lbs.'
    print(f'Your weight is: {round(weight, 1)} {unit}')
elif unit == 'L':
    weight /= 2.20462
    unit = 'kgs.'
    print(f'Your weight is: {round(weight, 1)} {unit}')
else:
    print(f'{unit} was not valid!')