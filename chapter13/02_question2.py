# Write a program to input name, marks and phone number of a student and format it
# using the format function like below:

name=input("enter your name: ")
marks=int(input("enter you marks: "))
number=int(input("enter your number: "))

s="The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,number)
print(s)