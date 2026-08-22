class mathUtils:

    @staticmethod
    def add(a,b):
        return a + b

    @classmethod
    def description(cls):
        print("This is utility class for maths operations")

n = mathUtils()
print(n.add(2,4))
print(n.description())
