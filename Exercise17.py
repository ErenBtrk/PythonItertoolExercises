'''

17. Write a Python program to read a given string character by character
and compress repeated character by storing the length of those character(s).
 
'''

def iter_func(iterable):
    iterator = iter(iterable)
    list1 = []
    element = iterable[0]
    count = 0
    i = 0
    while True:
        i += 1
        try:
            temp = element
            element = next(iterator)
            if(element == temp):
                count += 1
            else:
                tuple1 = (count,temp)
                list1.append(tuple1)
                count = 1
        except StopIteration:
            tuple1 = (count,temp)
            list1.append(tuple1)
            count = 1
            break
    return list1


print(iter_func("AAASSSSKKIOOOORRRREEETTTTAAAABBBBBBDDDDD"))
print(iter_func("jjjjiiiiooooosssnssiiiiwwwweeeaaaabbbddddkkkklll" ))

######################################################################################


from itertools import groupby
def encode_str(input_str):
    return [(len(list(n)), m) for m,n in groupby(input_str)]
 
str1 = "AAASSSSKKIOOOORRRREEETTTTAAAABBBBBBDDDDD" 
print("Original string:")
print(str1)
print("Result:")
print(encode_str(str1))

str1 = "jjjjiiiiooooosssnssiiiiwwwweeeaaaabbbddddkkkklll" 
print("\nOriginal string:")
print(str1)
print("Result:")
print(encode_str(str1))
