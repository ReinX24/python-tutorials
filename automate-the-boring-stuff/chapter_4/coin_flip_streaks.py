import random

head_streaks = 0
tail_streaks = 0
heads_tails_list = []

for experiment_number in range(100):
    # Code that creates a list of 100 'heads' or 'tails' values.
    if random.randint(0, 1) == 0:
        heads_tails_list.append("heads")
    else:
        heads_tails_list.append("tails")

    # Code that checks if there is a streak if 6 heads or tails in a row.
    if (
        "heads" not in heads_tails_list[len(heads_tails_list) - 6 :]
        and len(heads_tails_list) >= 6
    ):
        # print(heads_tails_list[len(heads_tails_list) - 6 :])
        # print("Tails 6 times in a row detected!")
        tail_streaks += 1
    elif (
        "tails" not in heads_tails_list[len(heads_tails_list) - 6 :]
        and len(heads_tails_list) >= 6
    ):
        # print(heads_tails_list[len(heads_tails_list) - 6 :])
        # print("Heads 6 times in a row detected!")
        head_streaks += 1

# print(heads_tails_list)
print(f"Chance of head streak: {head_streaks} / 100")
print(f"Chance of tail streak: {tail_streaks} / 100")
print(f"Chance of streak: {(head_streaks + tail_streaks) / 100}%")
