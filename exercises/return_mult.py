
def count(lst):
    above_five, belowe_five = 0, 0
    for x in lst:
        if len(x) > 5:
            above_five += 1
        else:
            belowe_five += 1

    return above_five, belowe_five

lst_names = []
print("Enter 10 Random Names")

while len(lst_names)<10:
    lst_names.append(str(input("\nname: ")))

ab, be = count(lst_names)

print("Above 5 letter names: {} \nBelow 5 letter names: {}".format(ab, be))