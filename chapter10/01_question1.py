# Create a class “Programmer” for storing information of few programmers
# working at Microsoft.


class Programmer:
    job="microsoft"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary


tilak= Programmer("tilak",120000)
print(tilak.name,tilak.job,tilak.salary)


ravi= Programmer("ravi",10000)
print(ravi.name,ravi.job,ravi.salary)

sahil= Programmer("sahil",50000)
print(sahil.name,sahil.job,sahil.salary)