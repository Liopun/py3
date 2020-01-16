import array
import random


def reverse_array(new_arr):
    i_start, i_end = 0, (len(new_arr) - 1)
    for x in new_arr:
        new_arr[i_start] = new_arr[i_end]
        i_start += 1
        i_end -= 1
    return new_arr


def array_del(arr, index):
    new_arr = []
    for x in arr:
        if x != arr[index]:
            new_arr.append(x)
    print("Old Array: %s \nNew Array (Remove index %d): %s \nReversed New Array: %s" % (
    arr, index, new_arr, reverse_array(new_arr)))


array_int = []
while len(array_int) < 5:
    array_int.append(random.randint(1, 100))
array_del(array_int, 4)
