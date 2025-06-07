def russian_peasant(a, b):
    result = 0
    while b > 0:
        if b % 2 != 0:
            result += a
        a = a * 2  # doubling the multiplicant
        b = b // 2 # halving  the other multplicant
    return result

# testing with negative number (limitation)
a = -18
b = 7
try:
    print("\n\nResult:", russian_peasant(a, b))
except Exception as e:
    print("\n\nError occurred:", e)
