'''
13. Write a Python program to chose specified number of colours from three
different colours and generate all the combinations with repetitions.
 
'''

from itertools import combinations_with_replacement

def generate(iterable,length):
    return list(combinations_with_replacement(iterable,length))

colours = ["Red","Green","Blue"]

print(generate(colours,1),"\n")
print(generate(colours,2),"\n")
print(generate(colours,3),"\n")

