# Write __str__() method to print the vector as follows:
#  7i + 8j +10k 


class Vector:

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self,other):
        result=Vector(self.x+other.x,self.y+other.y,self.z+other.z)
        return result
    
    def __str__(self):
        return f"{self.x}i+{self.y}j+{self.z}z"
    
a=Vector(3,4,5)
b=Vector(4,4,5)

print(a+b)