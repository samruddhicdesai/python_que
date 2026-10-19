numbers = [1,2,3,4,5,5,4,3]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
print(largest)