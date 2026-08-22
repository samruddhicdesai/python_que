def safe_divide(a,b):
    if b == 0:
        print("b should not be zero")
        print("Cannot divide by zero")
    return a/b

print(safe_divide(2,2))
print(safe_divide(2,0))