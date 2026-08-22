try:
    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))

    if num1 < 0 or num2 <0:
        raise ValueError("DO not enter negative numbers")
    
    print(num1/num2)

except ValueError:
    print("Please enter a vaild number.")

except ZeroDivisionError:
    print("Cannot divide by zero")

