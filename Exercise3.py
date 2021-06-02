'''
3. Write a Python program to generate the running maximum, minimum value of the elements of an iterable.

'''

def iter_func_max(iterable):
    iterator = iter(iterable)
    maxValue = next(iterator)
    print(f"maximum value = {maxValue}")
    while True:
        try:
            element = next(iterator)
            if(element > maxValue):
                maxValue = element
                print(f"maximum value = {maxValue}")
            else:
                print(f"maximum value = {maxValue}")
        except StopIteration:
            break

def iter_func_min(iterable):
    iterator = iter(iterable)
    minValue = next(iterator)
    print(f"minimum value = {minValue}")
    while True:
        try:
            element = next(iterator)
            if(element < minValue):
                minValue = element
                print(f"minimum value = {minValue}")
            else:
                print(f"minimum value = {minValue}")
        except StopIteration:
            break

list1 = [1,3,2,7,9,8,10,11,12,14,11,12,7]
iter_func_max(list1)
print("\n\n")

list2 = [3,2,7,9,8,10,11,12,1,14,11,12,7]
iter_func_min(list2)

#######################################################################


from itertools import accumulate
def running_max_product(iters):
    return accumulate(iters, max)
#List
result = running_max_product([1,3,2,7,9,8,10,11,12,14,11,12,7])
print("Running maximum value of a list:")
for i in result:
    print(i)
#Tuple
result = running_max_product((1,3,3,7,9,8,10,9,8,14,11,15,7))
print("Running maximum value of a Tuple:")
for i in result:
    print(i)
def running_min_product(iters):
    return accumulate(iters, min)
#List
result = running_min_product([3,2,7,9,8,10,11,12,1,14,11,12,7])
print("Running minimum value of a list:")
for i in result:
    print(i)
#Tuple
result = running_min_product((1,3,3,7,9,8,10,9,8,0,11,15,7))
print("Running minimum value of a Tuple:")
for i in result:
    print(i)
