numbers = [1,2,2,3,4,3,2,4,5]
result = []

for n in numbers:
    if n not in result:
        result.append(n)

print(result)