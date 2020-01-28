from datetime import date

# Q1: The year that u will turn 100 years old

try:
    name = str(input("Enter ur name(string): "))
    age = int(input("Enter ur age(number): "))

except ValueError as e:
    print("Invalid input", e)


today = date.today()
remainder = 100 - age

print("%s is going to be 100 years old in %d" % (name, today.year + remainder))

