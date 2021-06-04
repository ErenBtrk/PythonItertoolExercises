'''

12. Write a Python program to create Cartesian product of two or more given lists using itertools.

'''

def generate(list1,list2):
    for item1 in list1:
        for item2 in list2:
            tuple1 = (item1,item2)
            yield tuple1

list1 = [1,2]
list2 = [3,4,5]

for i in generate(list1,list2):
    print(i)

print("---------------------------------------")

list3 = [1,2,3]
list4 = [3,4,5]

for i in generate(list3,list4):
    print(i)

###########################################################################################

# import itertools 
# def cartesian_product(lists):
#     return list(itertools.product(*lists))

# ls = [[1,2],[3,4]]
# print("Original Lists:",ls)
# print("Cartesian product of the said lists: ",cartesian_product(ls))
# ls = [[1,2,3],[3,4,5]]
# print("\nOriginal Lists:",ls)
# print("Cartesian product of the said lists: ",cartesian_product(ls))
# ls = [[],[1,2,3]]
# print("\nOriginal Lists:",ls)
# print("Cartesian product of the said lists: ",cartesian_product(ls))
# ls = [[1,2],[]]
# print("\nOriginal Lists:",ls)
# print("Cartesian product of the said lists: ",cartesian_product(ls))