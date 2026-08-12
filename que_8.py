num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print('''
Enter the number for the operations:
1. for addition(+)
2. for subtraction(-)
3. for multiplication(*)
4. for division(/)
''')

operation = int(input("Enter the number for the operation : "))
match(operation):
    case 1:
        print("Addition : ",num1 + num2)

    case 2:
        print("Subtraction : ",num1 - num2)

    case 3:
        print("Multication : ",num2 * num2)

    case 4:
        print("Division: ", num1 / num2)

    case _:
        print("Enter the number form the given option")
 