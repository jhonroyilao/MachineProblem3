import time 

def russian_peasant(a, b):
    result = 0
    while b > 0:
        if b % 2 != 0: # if b is odd
            result += a
        a = a * 2  # doubling the multiplicant
        b = b // 2 # halving  the other multplicant
    return result

# testing with negative number (limitation)
a = 150
b = -5
try:
    print("\n\nResult:", russian_peasant(a, b))
except Exception as e:
    print("\n\nError occurred:", e)


start_time = time.time()
end_time = time.time()
print("\n\nTime taken:", end_time - start_time, "seconds\n\n\n")