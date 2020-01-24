from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odds = list(filter(lambda n : n%2!=0, nums))

triples = list(map(lambda n : n*3, odds))

sum = reduce(lambda a, b : a+ b , triples)

print(odds, triples, sum)