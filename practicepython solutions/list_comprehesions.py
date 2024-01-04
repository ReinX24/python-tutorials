def main():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print(eval_even_list(a))


def eval_even_list(num_list):
    """Return a list with only even numbers."""
    return [num for num in num_list if num % 2 == 0]


if __name__ == "__main__":
    main()
