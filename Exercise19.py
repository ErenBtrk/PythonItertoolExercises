'''
19. Write a Python program which iterates the integers from 1
to a given number and print "Fizz" for multiples of three, 
print "Buzz" for multiples of five, print "FizzBuzz" for
multiples of both three and five using itertools module.

'''

def generate(endNum):
    for i in range(1,endNum):
        flag1 = False
        flag2 = False
        
        if(i % 3 == 0):
            flag1 = True
        else:
            flag1 = False

        if(i % 5 == 0):
            flag2 = True
        else:
            flag2 = False

        if(flag1 == True and flag2 == False):
            yield "Fizz"
        elif(flag1 == False and flag2 == True):
            yield "Buzz"
        elif(flag1 == True and flag2 == True):
            yield "FizzBuzz"
        else:
            yield i

for i in generate(100):
    print(i)

print("**********************")
###############################################################################################

import itertools as it
 
def fizz_buzz(n):
    fizzes = it.cycle([""] * 2 + ["Fizz"])
    buzzes = it.cycle([""] * 4 + ["Buzz"])
    fizzes_buzzes = (fizz + buzz for fizz, buzz in zip(fizzes, buzzes))
    result = (word or n for word, n in zip(fizzes_buzzes, it.count(1)))
    for i in it.islice(result, 100):
        print(i)

n = 50
fizz_buzz(n)
