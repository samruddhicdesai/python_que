class empolyee:
     def __init__(self,salary):
        self.salary = salary

     @property
     def salary(self):
        return self._salary

     @salary.setter
     def salary(self,value):
        if value < 0:
            print("warning : salary cannot be negative")

        else:
            self._salary = value

emp = empolyee(30000)
print(emp.salary)

emp.salary(-50000)
print(emp.salary)
