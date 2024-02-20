import random
import sys


if __name__ == "__main__":
    print("ROCK, PAPER, SCISSORS")

    # Stores wins, losses, and ties by the player.
    wins = 0
    losses = 0
    ties = 0

    while True:  # The main game loop.
        print(f"{wins} Wins, {losses} Losses, {ties} Ties")

        # Ask the user for their choice and print their choice.
        while True:
            print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
            user_move = input()

            if user_move == "r":
                print("ROCK versus...")
                break
            elif user_move == "p":
                print("PAPER versus...")
                break
            elif user_move == "s":
                print("SCISSORS versus...")
                break
            elif user_move == "q":
                sys.exit()  # Quit the program.
            else:
                print("Type one of r, p, s, or q.")

        computer_move = random.randint(
            0, 2
        )  # random number between 0 and 2 (both included)

        # Display what the computer chose:
        if computer_move == 0:
            computer_choice = "r"
            print("ROCK")
        elif computer_move == 1:
            computer_choice = "p"
            print("PAPER")
        elif computer_move == 2:
            computer_choice = "s"
            print("SCISSORS")

        # Display and record the win/loss/tie:
        if user_move == "r" and computer_choice == "s":
            wins += 1
            print("You win!")
        elif user_move == "p" and computer_choice == "r":
            wins += 1
            print("You win!")
        elif user_move == "s" and computer_choice == "p":
            wins += 1
            print("You win!")
        elif user_move == computer_choice:
            ties += 1
            print("It is a tie!")
        else:
            losses += 1
            print("You lose!")
