'''
9. Write a Python program to split an iterable
and generate iterables specified number of times.

'''

def generate(iterable,numberOfTimes):
    for i in range(numberOfTimes):
        yield iterable

list1 = [1,2,3,4,5]

for i in generate(list1,5):
    print(list(i),id(i))

str1 = "Python itertools"

for i in generate(str1,3):
    print(list(i),id(i))


#######################################################################

import itertools as it
def tee_data(iter, n):
    return it.tee(iter, n)
#List
result = tee_data(['A','B','C','D'], 5)
print("Generate iterables specified number of times:")
for i in result:
    print(list(i))

#String
result = tee_data("Python itertools", 4)
print("\nGenerate iterables specified number of times:")
for i in result:
    print(list(i))