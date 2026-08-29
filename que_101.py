year = int(input("Enter the year: "))

if year % 4 == 0 and year % 100 !=1 or year % 400 == 0:
    print("Leap yaer")
else:
    print("Not a leap year")