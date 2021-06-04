'''
15. Write a Python program to generate all possible permutations of n different objects.

'''

from itertools import permutations

def perm(iterable):
    for item in permutations(iterable):
        print(item)

perm([1,2])
perm([1,2,3])