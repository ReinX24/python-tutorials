import time, sys

indent = 0  # How many spaces to indent.
indent_increasing = True  # Whether the indentation is increasing or not.

try:
    while True:  # The main program loop.
        print(" " * indent, end="")  # prints indent line before asterisks
        print("********")
        time.sleep(0.1)  # Pause for 1/10 of a second.

        if indent_increasing:
            # Increase the number of spaces
            indent += 1
            if indent == 20:
                indent_increasing = False

        else:
            # Decrease the number of spaces:
            indent -= 1
            if indent == 0:
                # Change direction, go back to incrementing indents.
                indent_increasing = True

except KeyboardInterrupt:
    sys.exit()
