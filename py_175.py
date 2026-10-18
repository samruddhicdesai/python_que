def greet(name, msg="Hello"):
    print(msg, name)

greet("Sam")                  # Default argument
greet("Sam", "Welcome")       # Positional arguments
greet(msg="Hi", name="Sam")   # Keyword arguments