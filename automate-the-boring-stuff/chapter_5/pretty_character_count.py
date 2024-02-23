from email import message_from_file
import pprint

message = "It was a bright cold day in April, and the clocks were striking thirteen."

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

# pprint.pprint(count)
pretty_result = pprint.pformat(count)  # for storing in strings
print(pretty_result)
