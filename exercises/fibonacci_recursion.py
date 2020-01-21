# Fibonacci Sequence
def fib(x):
    if x < 0:
        print("Incorrect Input!")
    elif x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


fib_input = int(input("\nEnter A Number: "))
print(fib(fib_input))
