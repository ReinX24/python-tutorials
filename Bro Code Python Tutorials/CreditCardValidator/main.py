# Python credit card validator program

# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
#       (If result is a two-digit number,
#       add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid

# 1234-5678-9012-3456

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1
card_number = input('Enter a credit card #: ')
card_number = card_number.replace('-', '')
card_number = card_number.replace(' ', '')
card_number = card_number[::-1]
print(card_number)

# Step 2
for i in card_number[::-2]:
    sum_odd_digits += int(i)

# Step 3
for i in card_number[1::2]:
    i = int(i * 2)
    # resume at 6:07
