# Write a program to print multiplication table of n using for loops in reversed
# order

n=int(input("enter any number: "))

for i in range(1,11):
    print(f"{n} * {11-i} = {n*(11-i)}")