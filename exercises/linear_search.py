pos = -1


def search(ls, n):
    for x in ls:
        if x == n:
            globals()['pos'] = ls.index(x)
            return True

    return False


the_list = [5, 8, 4, 6, 9, 2]
num = 9

if search(the_list, num):
    print("Found at ", pos + 1)
else:
    print("Not Found")
