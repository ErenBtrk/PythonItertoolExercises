'''
10. Write a Python program to create an iterator
to get specified number of permutations of elements.

'''

from itertools import permutations

def generate(iterable,numberOfPerm):
    for item in iterable:
        yield list(permutations(item,numberOfPerm))


list1 = [['A','B','C','D'],[1,2,3,4,5],"C++"]    

for i in generate(list1,2):
    print(i)


