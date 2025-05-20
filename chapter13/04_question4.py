# Write a program to filter a list of numbers which are divisible by 5


def divisible5(n):
    if(n%5==0):
        return True
    return False

a=[55,3434,53,15,344,100,45]

f=list(filter(divisible5,a))
print(f)