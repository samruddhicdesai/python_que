numbers = [11,24,7,18,31,40,13]
largest = numbers[0]
for num in numbers:
    if num % 2 == 0:
        if num > largest:
             largest = num

print(largest)