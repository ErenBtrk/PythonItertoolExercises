'''
5. Write a Python program to generate an infinite cycle of elements from an iterable. 

'''

import itertools

list1 = [1,2,3,4,5]

iterator = iter(list1)

while True:
    element = next(iterator)
    print(element)
    if(element == list1[len(list1)-1]):
        iterator = iter(list1)
        
############################################################################

# import itertools as it
# def cycle_data(iter):
#     return it.cycle(iter)
# # Following  loops will run for ever    
# #List
# result = cycle_data(['A','B','C','D'])
# print("The said function print never-ending items:")
# for i in result:
#     print(i)

# #String
# result = cycle_data('Python itertools')
# print("The said function print never-ending items:")
# for i in result:
#     print(i)