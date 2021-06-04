'''

6. Write a Python program to make an iterator that drops elements 
from the iterable as soon as an element is a positive number. 

'''

def iter_func(iterable):
    iterator = iter(iterable)
    count = 0
    while True:
        try:
            element = next(iterator)
            if(element > 0):
                count2 = 0
                while count2 < count:
                    iterable.pop(0)
                    count2 += 1
                break 
            else:
                count += 1
        except StopIteration:
            break


list1 = [-1,-2,-3,4,-10,2,0,5,12]
iter_func(list1)
print(list1)
##########################################################################################

import itertools as it
def drop_while(nums):
    return it.dropwhile(lambda x : x < 0, nums)
nums = [-1,-2,-3,4,-10,2,0,5,12]
print("Original list: ",nums)
result = drop_while(nums)
print("Drops elements from the iterable when a positive number arises \n",list(result))
#Alternate solution
def negative_num(x):
    return x < 0
def drop_while(nums):
    return it.dropwhile(negative_num, nums)
nums = [-1,-2,-3,4,-10,2,0,5,12]
print("Original list: ",nums)
result = drop_while(nums)
print("Drops elements from the iterable when a positive number arises \n",list(result))