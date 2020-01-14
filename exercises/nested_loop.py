def hash_print():
    for y in range(1, 5):
        hash, hash_asc, hash_desc = "", "\t\t", "\t\t"
        for x in range(1, 5):
            hash += "#"
        for x in range(0, y):
            hash_asc += "#"
        for x in range(0, 5 - y):
            hash_desc += "#"
        print(hash + hash_asc + hash_desc, "\n")


hash_print()
