numbers = [12,7,8,15,20,3,6]

even = 0
odd = 0

for n in numbers :
    if n % 2== 0:
        even += 1
    if n % 2 != 0:
        odd += 1
print(even)
print(odd)