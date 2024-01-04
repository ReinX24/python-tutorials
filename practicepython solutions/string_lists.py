def main():
    """Main method."""
    print(is_palindrome("racecar"))


def is_palindrome(base_str):
    """Check if a string is a palindrome or not."""
    return base_str == base_str[::-1]


if __name__ == "__main__":
    main()
