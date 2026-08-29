n = int(input("Enter number: "))

rev = 0
temp = n

while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

print("Palindrome" if n == rev else "Not palindrome")