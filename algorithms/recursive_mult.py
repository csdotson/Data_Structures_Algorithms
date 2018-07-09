'''
Problem: Recursively multiply two n-digit numbers. Numbers will have a length that is a power of 2 (i.e. 4, 8, 16... digits)
'''
def recursive_mult(x, y):
    if len(str(x)) <= 1:
        return x * y 

    n = len(str(x))
    a, b = int(str(x)[:n//2]), int(str(x)[n//2:])
    c, d = int(str(y)[:n//2]), int(str(y)[n//2:])

    return ((10**n)*recursive_mult(a, c) + (10**(n/2))*(recursive_mult(a, d) + recursive_mult(b, c)) + recursive_mult(b, d))