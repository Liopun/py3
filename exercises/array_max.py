import random

arr1 = []


def find_max(arr):
    mux = 0
    for x in arr:
        mux = x if x >= mux else mux
    print("Array: %s \nMax: %d" % (arr, mux))


while len(arr1) < 5:
    arr1.append(random.randint(1, 100))
find_max(arr1)
