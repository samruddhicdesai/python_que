class student:
    def __init__(self , name , marks ):
        self.name = name
        self.marks = marks

    def calculate(self):
        total = sum(self.marks)
        average = total/3

        print("Total:",total)
        print("Average:",average)

        if average >= 40:
            print("Pass")
        else:
            print("Fail")

s = student("Rahul",[70,80,90])
s.calculate()
