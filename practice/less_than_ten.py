# Q3: List Less Than Ten

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lst = []

for x in a:
    if x < 10:
        lst.append(x)

print("Less than 10: ", lst)