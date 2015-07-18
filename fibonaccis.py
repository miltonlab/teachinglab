def fib_linear(n):
    a = 1
    b = 1
    print (a)
    for i in range(n):
        print (b)
        aux = b
        b = a + b
        a = aux

def fib_py(n):
    a = b = 1
    for i in range(n):
        print(b)
        a, b = b, a + b

def fib_recursive(n):
    if n < 3:
        return 1
    else:
        print (n)
        return fib_recursive(n - 1) + fib(n - 2)

if __name__ == "__main__":
    fib_py(5)