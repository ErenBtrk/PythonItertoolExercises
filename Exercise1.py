'''
1. Write a Python program to create an iterator from several iterables
in a sequence and display the type and elements of the new iterator.

'''

def iterFunc(iterable):
    iterator = iter(iterable)
    while True:
        try:
            element = next(iterator)
            new_iterator = iter(element)
            print(new_iterator)
            while True:
                try:
                    new_element = next(new_iterator)
                    print(new_element)
                except StopIteration:
                    break
        except StopIteration:
            break

list1 = [[1,2,3,4,5,6],["ali","veli","isa","musa"],[True,True,False]]
iterFunc(list1)

tuple1 = ((1,2,3),("ayse","fatma"),(False,True))
iterFunc(tuple1)

############################################################################

from itertools import chain
def chain_func(l1,l2,l3):
    return chain(l1,l2,l3)    
#List
result = chain_func([1,2,3], ['a','b','c','d'], [4,5,6,7,8,9])
print("Type of the new iterator:")
print(type(result))
print("Elements of the new iterator:")
for i in result:
    print(i)

#Tuple
result = chain_func((10,20,30,40), ('A','B','C','D'), (40,50,60,70,80,90))
print("Type of the new iterator:")
print(type(result))
print("Elements of the new iterator:")
for i in result:
    print(i)
