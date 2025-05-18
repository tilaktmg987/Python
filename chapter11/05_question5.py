# Write a class vector representing a vector of n dimensions. Overload the + and *
# operator which calculates the sum and the dot(.) product of them.

class Vector:

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def __add__(self,other):
        result=Vector(self.x+other.x,self.y+other.y,self.z+other.z)
        return result
    
    def __mul__(self,other):
        result=Vector(self.x*other.x,self.y*other.y,self.z*other.z)
        return result
    
    def __str__(self):
        return f"Vector({self.x},{self.y},{self.z})"

a=Vector(1,2,3)
b=Vector(1,2,3)

print(a+b)
print(a*b)