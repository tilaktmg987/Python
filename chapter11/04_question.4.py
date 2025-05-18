# Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.

# 3i+1

class Complex:

    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def __add__(self,another):
        return f"{self.real+another.real}+{self.img+another.img}i"
    
    def __mul__(self,another):
        return f"{self.real*another.real}+{self.img*another.img}i"


c1=Complex(1,3)
c2=Complex(1,3)
print(c1+c2)
print(c1*c2)