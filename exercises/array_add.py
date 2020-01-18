import random
import numpy as np


arr1, arr2 = np.array([]), np.array([])


def adds(arg1, arg2):
    new_arr = np.array([])
    for x in np.arange(arg1.size):
        new_arr.append(arg1[x] + arg2[x])
    return new_arr


while len(arr1) < 5:
    arr1.append()
    arr1 = np.append(random.randint(1, 100))
    arr2.append()
    arr2 = np.append(random.randint(1, 100))

print("Arr 1: %s \nArr 2: %s \nAddition: %s" %(arr1, arr2, adds(arr1, arr2)))
