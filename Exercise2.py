'''
2. Write a Python program to generate the running product of the elements of an given iterable.

'''


def iter_func(iterable):
    product = 1
    iterator = iter(iterable)
    while True:
        try:
            element = next(iterator)
            product *= element
            print(product) 
        except StopIteration:
            break

list1 = [1,2,3,4,5,6]
iter_func(list1)

tuple1 = (5,10,15,20)
iter_func(tuple1)

#####################################################################

from itertools import accumulate
import operator
def running_product(it):
    return accumulate(it,operator.mul)

#List
result = running_product([1,2,3,4,5,6,7])
print("Running product of a list:")
for i in result:
    print(i)

#Tuple
result = running_product((1,2,3,4,5,6,7))
print("Running product of a Tuple:")
for i in result:
    print(i)
