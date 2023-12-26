from prime import is_prime

def test_is_prime(n, expected):
    """Test that takes in two parameters to check if n is a prime number."""
    if is_prime(n) != expected:
        print(f"ERROR on is_prime({n}), expected {expected}")