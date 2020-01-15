import array
import random


def array_del(arr, index):
    new_arr = []
    for x in arr:
        if x != arr[index]:
            new_arr.append(x)
    print("Old Array: %s \nNew Array (No index %d): %s" % (arr, index, new_arr))


array_int = []
while len(array_int) < 5:
    array_int.append(random.randint(1, 100))
array_del(array_int, 4)
