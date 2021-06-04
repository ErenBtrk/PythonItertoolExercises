'''
11. Write a Python program to generate combinations of a given length of given iterable.

'''

from itertools import combinations

def generate(iterable,length):
    for item in iterable:
        yield combinations(item,length)

list1 = [['A','B','C','D'],[1,2,3,4,5],"Java"]  

for i in generate(list1,2):
    print(list(i))