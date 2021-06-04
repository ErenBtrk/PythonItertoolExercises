'''

16. Write a Python program find the sorted sequence from a set of permutations of a given input.

'''

from itertools import permutations


def generate(iterable):
    for item in permutations(iterable):
        item = list(item)
        if(item == sorted(item)):
            print(item)
        

generate([12,10,9])
generate([2, 3, 1, 0])





