import time

my_time = int(input('Enter the time in seconds: '))

# Prints 1 to 3
# for x in range(0, my_time):
#     print(x + 1)
#     time.sleep(1)

# Prints 3 to 1
# for x in reversed(range(0, my_time)):
#     print(x + 1)
#     time.sleep(1)

# Another way of printing 3 to 1
# starting value, ending value (exclusive), and step value
# for x in range(my_time, 0, -1):
#     print(x)
#     time.sleep(1)

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    # :02 reserves 2 spaces using string formatting
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    # print('%02d:%02d:%02d' % (hours, minutes, seconds))
    time.sleep(1)
print('TIME\'S UP!')
