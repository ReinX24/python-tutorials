def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 35, 55, 89]

    # Returns a list of all numbers less than 5 all in one line
    print([x for x in a if x < 5])

    print(less_than_5(a))

    print(less_than_num(a, 3))
    print(less_than_num(a, 7))

    # Printing the first 12 fibonacci numbers
    # firstNum, secondNum = 1, 1
    # print(firstNum)
    # print(secondNum)
    # for i in range(10):
    #     nextNum = firstNum + secondNum
    #     firstNum = secondNum
    #     secondNum = nextNum
    #     print(nextNum)


def less_than_5(num_list):
    new_list = []
    for num in num_list:
        if num < 5:
            new_list.append(num)
    return new_list


def less_than_num(num_list, num_limit):
    """Return elements in num_list smallet than num_limit."""
    new_list = []
    for num in num_list:
        if num < num_limit:
            new_list.append(num)
    return new_list


if __name__ == "__main__":
    main()
