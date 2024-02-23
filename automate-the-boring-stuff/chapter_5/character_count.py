message = "It was a bright cold day in April, and the clocks were striking thirteen."

count = {}

for character in message:
    count.setdefault(character, 0)  # add a character and new count if the
    # character is not in count
    count[character] += 1  # increment count

print(count)
