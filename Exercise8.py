'''
8. Write a Python program to create an iterator that returns
consecutive keys and groups from an iterable.
 
'''

def iter_func(iterable):
    dict1 = {}
    iterator = iter(iterable)
    while True:
        try:
            element = next(iterator)
            if(element in dict1):
                dict1[element].append(element)
            else:
                new_list = []
                new_list.append(element)
                dict1[element] = new_list
        except StopIteration:
            break
    return dict1

str1 = 'AAAAJJJJHHHHNWWWEERRRSSSOOIIU'
new_dict = iter_func(str1)

for key,value in new_dict.items():
    print(f"key : {key}\ngroup : {value}")


list1 = [1,2,2,3,4,4,5,5,5,6,6,7,7,7,8]
new_dict = iter_func(list1)

for key,value in new_dict.items():
    print(f"key : {key}\ngroup : {value}")

####################################################################################

import itertools as it
print("Iterate over characters of a string and display\nconsecutive keys and groups from the iterable:")
str1 = 'AAAAJJJJHHHHNWWWEERRRSSSOOIIU'
data_groupby = it.groupby(str1)
for key, group in data_groupby:
    print('Key:', key)
    print('Group:', list(group))    
print("\nIterate over elements of a list and display\nconsecutive keys and groups from the iterable:")
str1 = 'AAAAJJJJHHHHNWWWEERRRSSSOOIIU'    
str1 = [1,2,2,3,4,4,5,5,5,6,6,7,7,7,8]
data_groupby = it.groupby(str1)
for key, group in data_groupby:
    print('Key:', key)
    print('Group:', list(group))
