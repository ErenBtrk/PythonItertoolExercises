'''
4. Write a Python program to construct an infinite iterator that returns
evenly spaced values starting with a specified number and step. 

'''

import itertools as it
start = 10
step = 1
print("The starting number is ", start, "and step is ",step)
my_counter = it.count(start, step)
# Following  loop will run for ever
print("The said function print never-ending items:")
for i in my_counter:    
    print(i)