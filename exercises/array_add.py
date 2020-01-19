import random
import array


arr1, arr2 = array.array('i', []), array.array('i', [])


def adds(arg1, arg2):
    new_arr = []
    for x in range(len(arg1)):
        new_arr.append(arg1[x] + arg2[x])
    return new_arr


while len(arr1) < 5:
    arr1.append(random.randint(1, 100))
    arr2.append(random.randint(1, 100))

print("Arr1: %s \nArr2: %s \nAddition: %s" %(arr1, arr2, adds(arr1, arr2)))
