num = int(input("Enter number : "))
total = 0

while num > 0:
    num = num % 10
    num //= 10
    num += 1

print(total)