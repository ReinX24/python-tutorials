import math

if __name__ == "__main__":
    # n = Nz^2 * p (1 - p) / (Nd^2 + z^2 * p (1 - p))
    print("[Lynch Formula Solver]")
    N = int(input("Enter N: "))
    d = float(input("Enter d: "))
    z = float(input("Enter z: "))
    p = 0.50
    n = (
        N
        * math.pow(z, 2)
        * p
        * (1 - p)
        / (N * math.pow(d, 2) + math.pow(z, 2) * 0.50 * (1 - 0.50))
    )
    print(f"n = {n} or n = {round(n)}")
