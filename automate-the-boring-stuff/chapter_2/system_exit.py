import sys


if __name__ == "__main__":
    while True:
        response = input("Type exit to exit ")
        if response == "exit":
            sys.exit()
        print(f"You typed {response}")
