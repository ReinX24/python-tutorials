from random import randint


def main():
    """Main method."""
    # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # Generating a list of random elements
    a = [randint(0, 10) for i in range(11)]
    b = [randint(0, 10) for i in range(13)]

    print(find_list_overlap(a, b))


def find_list_overlap(list_a, list_b):
    """Finding elements that are in list a and b."""
    overlap_list = []
    for element in list_a:
        if element in list_b and element not in overlap_list:
            overlap_list.append(element)
    return overlap_list


if __name__ == "__main__":
    main()
