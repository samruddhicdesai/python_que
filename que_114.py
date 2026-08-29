list = list(map(int,input().split()))
result = []
for num in list:
    if num not in result:
        result.append(num)

print(result)