import time

my_time = int(input('Enter the time in seconds: '))

# Prints 1 to 3
# for x in range(0, my_time):
#     print(x + 1)
#     time.sleep(1)

# Prints 3 to 1
for x in reversed(range(0, my_time)):
    print(x + 1)
    time.sleep(1)

print('TIME\'S UP!')
