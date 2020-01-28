# Q3:Divisors Finder


def div(num):
    divisors = []
    for x in range(1, num):
        if num % x == 0:
            divisors.append(x)
    return divisors


try:
    num = int(input("Divisors Finder\nEnter a number: "))
    print("The divisors of %d are %s" % (num, div(num)))
except ValueError as e:
    print("Invalid input", e)
except Exception as e:
    print("Error occurred", e)
