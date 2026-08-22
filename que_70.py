def decorator(function):
    def wrapper(*args,**kwargs):
        print("function is being")
        return function(*args,**kwargs)
    return wrapper

@decorator
def add(a,b):
    return a+b

print(add(10,20))