def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought += v.get(item, 0)  # gets the item value or returns 0
    return num_brought


if __name__ == "__main__":
    all_guests = {
        "Alice": {"apples": 5, "pretzels": 12},
        "Bob": {"ham sandwiches": 3, "apples": 2},
        "Carol": {"cups": 3, "apple pies": 1},
    }

    print(
        f"""The number of things being brought:
- Apples            : {total_brought(all_guests, 'apples')}
- Cups              : {total_brought(all_guests, 'cups')}
- Cakes             : {total_brought(all_guests, 'cakes')}
- Ham Sandwiches    : {total_brought(all_guests, 'ham sandwiches')}
- Apple Pies        : {total_brought(all_guests, 'apple pies')}"""
    )
