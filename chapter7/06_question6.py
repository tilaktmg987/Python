# Write a program to calculate the factorial of a given number using for loop

n=int(input("enter any number: "))
fac=1
for i in range(1,n+1):
    fac=fac*i
print(fac)