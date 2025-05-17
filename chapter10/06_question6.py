# Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.


class human:
    name="tilak"
    def greet(self):
        print(f"hello {self.name} ")


user1=human()

user1.greet()
