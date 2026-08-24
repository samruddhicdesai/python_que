numbers = [12,45,7,89,23,56]

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print(largest)