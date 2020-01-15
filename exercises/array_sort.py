import random
def array_sort(arr):
    print("Old Array: ", arr)
    print("Ascending Array: ", sorted(arr))
    print("Descending Array: ", sorted(arr, reverse=True))


array_int = []
while len(array_int) < 5:
    array_int.append(random.randint(1,100))
array_sort(array_int)
