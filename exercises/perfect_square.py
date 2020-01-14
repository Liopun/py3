import math
def pSquare():
    squareList = []
    for i in range(1, 500):
        sr = math.sqrt(i)
        if ((sr - math.floor(sr)) == 0):
            squareList.append(i)
    print(squareList)

pSquare()