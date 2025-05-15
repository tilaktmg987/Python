# Write a program which finds out whether a given name is present in a list or not.

fruits=["apple","banana","orange"]

name=input("enter your fruits: ")

if(name in fruits):
    print("fruits found in the list")
else:
    print("fruits not found in the list")