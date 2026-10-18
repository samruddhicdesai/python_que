class student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print(f"Name : {self.name} , Age : {self.age} , Marks : {self.marks}")

s1 = student("Sam",12,99)
s1.display() 