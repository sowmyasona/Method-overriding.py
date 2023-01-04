class parent():
    def walk(self):
        print("keep walking")

class child(parent):
    def walk(self):
        print('Need a break')

c=child()
c.walk()

c=parent()
c.walk()