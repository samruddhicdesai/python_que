day = int(input("Enter the number between 1 to 7 : "))

match(day):
    case 1 :
        print("Monday")

    case 2 :
        print("Tuesday")

    case 3:
        print("Wednesday")

    case 4:
        print("Thrusday")

    case 5:
        print("Friday")

    case 6:
        print("Saturday")

    case 7:
        print("Sunday")

    case _:
        print("Enter the between 1 to 7")
        print("Number is not between 1 to 7")