pos = -1


def search(ls, n):

    l_index = 0
    u_index = len(ls) - 1
    while l_index <= u_index:
        mid_index = (l_index + u_index) // 2
        if ls[mid_index] == n:
            globals()['pos'] = mid_index
            return True
        else:
            if ls[mid_index] < n:
                l_index = mid_index + 1
            else:
                u_index = mid_index - 1

    return False


the_list = [5, 8, 14, 16, 19, 21]
num = 21

if search(the_list, num):
    print("Found at ", pos + 1)
else:
    print("Not Found")
