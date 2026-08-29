list = list(map(int,input().split()))
min = list[0]
for num in list:
    if num < min:
        min = num
print(min)