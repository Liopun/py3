# Q1
# Checking If The Given Integer is Positive or Negative
def signChecker():
    num_1 = int(input("Enter a number: "))
    if (num_1 < 0):
        print(str(num_1) + " is a NEGATIVE number")
    else:
        print(str(num_1) + " is a POSITIVE number")

    signChecker()


signChecker()
