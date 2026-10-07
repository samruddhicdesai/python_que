numbers = [10,25,7,30,18]

largest = float('-inf')
second = float('-inf')

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second:
        second = num

print(second)