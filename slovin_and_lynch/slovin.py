import math

if __name__ == "__main__":
    # n = N / 1 + N * e^2
    print("[Slovin Formula Solver]")
    N = int(input("Enter N: "))
    e = float(input("Enter e: "))
    n = N / (1 + N * math.pow(e, 2))
    print(f"n = {n} or n = {round(n)}")
