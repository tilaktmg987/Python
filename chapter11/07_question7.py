# Override the __len__() method on vector of problem 5 to display the dimension of the
# vector.

class List:
    def __init__(self,l):
        self.l=l
    
    def __len__(self):
        return len(self.l)

a=List([1,2,3,4])

print(len(a))