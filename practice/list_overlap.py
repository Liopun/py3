import random
# List Overlap
# Generate 2 numbers for array size
size1, size2 = random.randint(1, 10), random.randint(1, 10)

# Generate 2 random lists
arr1 = random.sample(range(1, 100), size1)
arr2 = random.sample(range(1, 100), size2)


def compare(arr1, arr2):
    final = []
    for x in arr1:
        for y in arr2:
            if x == y and x not in final:
                final.append(x)
                continue

    return final


print("list 1: %s\nlist 2: %s" % (arr1, arr2))
print("Joined List (no duplicates): %s", compare(arr1, arr2))
