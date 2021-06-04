'''
14. Write a Python program generate permutations
of specified elements, drawn from specified values.

'''
from itertools import product 

def generate(iterable,n):
    for x in product(iterable,repeat=n):
        yield x

for i in generate("Red",1):
    print(i,end = ',')

print("\n-----------------------------------------\n")

for i in generate("Red",2):
    print(i,end = ',')

print("\n-----------------------------------------\n")

for i in generate("Red",3):
    print(i,end = ',')

