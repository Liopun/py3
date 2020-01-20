import numpy as np


arr1 = np.array([
        [1, 2, 3],
        [6, 4, 5],
        [1, 6, 7]
    ])

arr2 = np.array([
        [1, 2, 3],
        [6, 8, 5],
        [2, 6, 7]
    ])
arr3 = arr1.dot(arr2)
arr_mult = np.empty([3, 3])
summ = 0

for x in range(3):
    for y in range(3):
        for k in range(3):
            summ = summ + (arr1[x][k] * arr2[k][y])
        arr_mult[x][y] = summ
        summ = 0

print("Custom Fx Output: \n%s \nInbuilt Fx Output: \n%s" % (arr_mult, arr3))