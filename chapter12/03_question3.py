# . Write a list comprehension to print a list which contains the multiplication table of a
# user entered number.

list=[1,2,3,4,5,6,7,8,9,10]


n=int(input("enter any number:"))

list1=[n*item for item in list]
print(list1)