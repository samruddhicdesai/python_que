numbers = list(map(int, input("Enter any list: ").split()))

max = numbers[0]

for num in numbers:
    if num > max:
        max = num

print(max)