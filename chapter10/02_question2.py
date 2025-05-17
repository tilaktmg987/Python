# Write a class “Calculator” capable of finding square, cube and square root of a
# number.

class Calculator:
    def __init__(self,n):
        self.n=n
    
    def calculator(self):
        print(f"square of {self.n} is:{self.n*self.n}")
        print(f"cube of {self.n} is:{self.n*self.n*self.n}")
        print(f"square root of {self.n} is:{self.n ** 0.5}")


num=int(input("enter any number: "))

user1=Calculator(num)

user1.calculator()