class Demo:
    count = 0

    def instance_method(self):
        return "Uses instance"

    @classmethod
    def class_method(cls):
        return cls.count

    @staticmethod
    def add(a, b):
        return a + b