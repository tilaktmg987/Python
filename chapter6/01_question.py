# Write a program to find the greatest of four numbers entered by the user.

a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
d=int(input("enter fourth number:"))

if(a>=b and a>=c and a>=d):
    print("greater number:",a)
elif(b>=a and b>=c and b>=d):
    print("greater number:",b)
elif(c>=a and c>=b and c>=d):
    print("greater number:",c)
else:
    print("greater number",d)
