# Q7: List Comprehensions

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
a_nu = []
# Using for loop
#for x in a:
#    if x % 2 == 0:
#        a_nu.append(x)

# One-line solution
a_nu = [num for num in a if num % 2 == 0]

print("Old List: %s \nEven List: %s" % (a, a_nu))
