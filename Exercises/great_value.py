def three_comp():
    try:
        print("Finding The Greatest Number \n")
        num_1 = int(input("Enter Ur 1st Number: "))
        num_2 = int(input("Enter Ur 2nd Number: "))
        num_3 = int(input("Enter Ur 3rd Number: "))

        if (num_1 > num_2 and num_1 > num_3):
            print(str(num_1) + " is the greatest value from them.")
        elif (num_2 > num_1 and num_2 > num_3):
            print(str(num_2) + " is the greatest value from them.")
        else :
            print(str(num_3) + " is the greatest value from them.")
    except ValueError:
        print("That Was Not A Valid Number, Lets try again!")
    three_comp()

three_comp()