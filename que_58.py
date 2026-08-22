import time

def timer(function):
    def wrapper():
        start = time.time()

        function()

        end = time.time()

        print("Exection time :",end - start,"seconds")

    return wrapper

@timer
def sum_number():
    total = 0

    for i in range(1,1000001):
        total += i

    print("Sum",total)

sum_number()