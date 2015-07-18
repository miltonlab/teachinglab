# version linear
def factorial1(n):
    f = 1
    for i in range(1, n+1):
        f *= i

# version recursiva
def factorial2(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    n = 5
    print ('El factorial de {0} es {1}: '.format(n, factorial1(n)))