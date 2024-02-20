import time, sys

indent_amount = 0
indent_increasing = True

try:
    while True:
        print(" " * indent_amount, end="")
        print("*******")
        time.sleep(0.2)

        if indent_increasing:
            indent_amount += 1
            if indent_amount == 20:
                indent_increasing = False
        else:
            indent_amount -= 1
            if indent_amount == 0:
                indent_increasing = True
except KeyboardInterrupt:
    print("Program Terminated...")
    sys.exit()
