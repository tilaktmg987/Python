# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class number:
    a=5

object=number()
object.a=0
print(object.a)