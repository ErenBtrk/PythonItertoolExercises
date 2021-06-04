'''

7. Write a Python program to make an iterator that drops elements from the iterable
as long as the elements are negative; afterwards, returns every element.
 
'''

def iter_func(iterable):
    iterator = iter(iterable)
    count = 0
    while True:
        try:
            element = next(iterator)
            if(element < 0):
                count2 = 0
                while(count2 <= count):
                    iterable.pop(0)
                    count2 += 1
            else:
                count += 1
        except StopIteration:
            break
    return iterable

list1 = [-1,-2,-3,4,-10,2,0,5,12]
new_list = iter_func(list1)
print(new_list)

############################################################################


import itertools as it
def drop_while(nums):
    return it.takewhile(lambda x : x < 0, nums)
nums = [-1,-2,-3,4,-10,2,0,5,12]
print("Original list: ",nums)
result = drop_while(nums)
print("Drop elements from the said list as long as the elements are negative\n",list(result))
#Alternate solution
def negative_num(x):
    return x < 0
def drop_while(nums):
    return it.dropwhile(negative_num, nums)
nums = [-1,-2,-3,4,-10,2,0,5,12]
print("Original list: ",nums)
result = drop_while(nums)
print("Drop elements from the said list as long as the elements are negative\n",list(result))