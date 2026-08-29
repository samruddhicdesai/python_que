class parent:
    def show(self):
        print("This is parent class")
class child(parent):
    def display(self):
        print("This is child class")

s = child()
s.show()
s.display()