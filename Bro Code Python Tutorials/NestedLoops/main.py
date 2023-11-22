# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

# for x in range(3):
#     for y in range(1, 10):
#         print(y, end=" ")
#     print()

rect_rows = int(input('Enter the # of rows: '))
rect_col = int(input('Enter the # of columns: '))
rect_symbol = input('Enter a symbol to use: ')

for x in range(rect_rows):
    for y in range(rect_col):
        print(rect_symbol, end=" ")
    print()
