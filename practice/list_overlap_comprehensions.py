import random

# Q10: List Overlap Comprehensions
# Generate 2 numbers for array size
size1, size2 = random.randint(1, 10), random.randint(1, 10)
arr_join = []

# Generate 2 random lists
arr1 = random.sample(range(1, 100), size1)
arr2 = random.sample(range(1, 100), size2)

arr_join = [a for a in arr1 for b in arr2 if (a == b) and a not in arr_join]

print("Array 1: %s \nArray 2: %s" % (arr1, arr2))
print("Joined List (no duplicates):", arr_join)