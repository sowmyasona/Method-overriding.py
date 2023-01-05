class Parent:     # parent class or main class
    def name(self):
        print("It is a parent class")
        
class Child(Parent):    # child class or sub class
    def name(self):
        print('It is a child class')

c=Child()
c.name()

c=Parent()
c.name()