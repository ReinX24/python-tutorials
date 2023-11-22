triangle_height = 5

for i in range(triangle_height):

    for j in range(triangle_height - i):
        print(' ', end='')

    for k in range(2 * i + 1):
        print('*', end='')
    print()
