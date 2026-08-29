n = int(input("Enter number:"))
sum = 0
temp = n
order = len(str(n))
while temp > 0:
    digits = temp % 10
    sum += digits ** order
    temp //= 10
print("Armstrong" if n == sum else "Not Armstrong")


