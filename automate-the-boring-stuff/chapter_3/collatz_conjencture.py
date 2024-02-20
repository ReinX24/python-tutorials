def collatz(inserted_num):
    if inserted_num % 2 == 0:
        return inserted_num // 2
    else:
        return 3 * inserted_num + 1


if __name__ == "__main__":
    try:
        print("Enter number:")
        user_number = int(input())
        while user_number != 1:
            user_number = collatz(user_number)
            print(user_number)
    except ValueError:
        print("Invalid input, please enter an integer.")
