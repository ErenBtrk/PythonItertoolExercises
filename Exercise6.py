'''

6. Write a Python program to make an iterator that drops elements 
from the iterable as soon as an element is a positive number. 

'''

def iter_func(iterable):
    iterator = iter(iterable)
    while True:
        try:
            element = next(iterator)
            if(element > 0):
                print(element)
        except StopIteration:
            break


list1 = [-1,2,5,-3,-8,10,-5,0]
iter_func(list1)