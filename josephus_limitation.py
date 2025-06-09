import sys
sys.setrecursionlimit(10**6)

# recursive josephus function
def josephus(n, k):
    if n == 1:
        return 0
    else:
        return (josephus(n - 1, k) + k) % n

# demonstrating limitation for large n
try:
    n = 100000000  # large number of people
    k = 2
    print("\n\nSafe position for large n:", josephus(n, k))


except RecursionError:
    print("RecursionError: Maximum recursion depth exceeded!")
