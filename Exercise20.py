'''
20. Write a Python program to find the factorial of a number using itertools module.

'''

def generate(number):
    for i in range(0,number+1):
        fact = 1
        for x in range(1,i+1):
            fact *= x
        yield fact

list1 = []
for i in generate(5):
    list1.append(i)

print(list1)

list1.clear()
for i in generate(9):
    list1.append(i)

print(list1)

#################################################################################

import itertools as it
import operator as op

def factorials_nums(n):
    result = list(it.accumulate(it.chain([1], range(1, 1 + n)), op.mul))
    return result
    
 
print("Factorials of 5 :", factorials_nums(5))
print("Factorials of 9 :", factorials_nums(9))