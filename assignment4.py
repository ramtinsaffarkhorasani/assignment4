a=int(input())
def is_factorial(n):
    i = f = 1
    while f < n:
        i += 1
        f *= i
    return f == n
c= is_factorial(a)
print(c)