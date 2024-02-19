import random


if __name__ == "__main__":
    random_num = random.randint(1, 20)
    guess_count = 0

    print("I am thinking of a number between 1 and 20.")

    while guess_count < 7:
        print("Take a guess")
        user_num = int(input())

        if user_num < random_num:
            print("Your guess is too low.")
            guess_count += 1
        elif user_num > random_num:
            print("Your guess is too high.")
            guess_count += 1
        else:
            break

    if user_num == random_num:
        print(f"Good job! You guessed my number in {guess_count} guesses!")
    else:
        print(f"Nope. The number I was thinking of was {random_num}.")
