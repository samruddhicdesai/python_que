def decorator(say_hello):
    def wrapper():
        print("Function is being called")
        say_hello()
    return wrapper
@decorator
def say_hello():
    print("Hello!")

say_hello()