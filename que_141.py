numbers = [15,4,28,2,19]

smallest = numbers[0]

for num in numbers:
    if smallest > num:
        smallest = num

print(smallest)
