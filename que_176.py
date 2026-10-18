square = lambda x: x * x
print(square(5))

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

squares = [x * x for x in range(1, 6)]