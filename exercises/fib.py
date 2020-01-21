
def fib(n):
    a, b = 0, 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)

        for x in range(2, n):
            c = a + b
            a = b
            b = c
            if c < n:
                print(c)
            else:
                continue


fib(5)
