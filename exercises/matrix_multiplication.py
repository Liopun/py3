import numpy as np

arr1 = np.array([
        [1,2,3],
        [4,5,6]
    ])

arr2 = np.array([
        [7,2],
        [4,6],
        [2,3]
    ])
arr_mult = np.empty([2,2])
sum = 0

for x in range(2):
    for y in range(2):
        for k in range(3):
            sum = sum + arr1[x][k] + arr2[k][y]
        arr_mult[x][y] = sum
        sum = 0

print(arr_mult)
        