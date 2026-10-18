class Student:
    college = "DYPCET"      # Class variable

    def __init__(self, name):
        self.name = name    # Instance variable

s1 = Student("Sam")
s2 = Student("Aarav")

print(s1.name)
print(s2.name)
print(s1.college)