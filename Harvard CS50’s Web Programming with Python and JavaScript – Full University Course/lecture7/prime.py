import math


def is_prime(n):
    """Checks if a number is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        # Check for other factors of n.
        if n % i == 0:
            return False
    # Return True if no other factors of n other than 1 and n itself is found, 
    # this means that n is a prime number.
    return True

# print(is_prime(7))
