numbers = [1,2,3,3,4,3,5]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)