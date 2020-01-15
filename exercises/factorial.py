def fact(n):
    factor = 1
    for x in range(1, n + 1):
        factor = factor * x
    print("The factorial of %d is %d" % (n, factor))


fact(int(input("Enter a Number to Get its Factorial: ")))
