# Write a program to find the maximum of the numbers in a list using the reduce
# function.


from functools import reduce
list=[1,2,3,4,5,6,7]

def function1(a,b):
    if(a>b):
        return a
    return b

print(reduce(function1,list))