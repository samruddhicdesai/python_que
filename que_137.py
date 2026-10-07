a = int(input("ENter num: "))
b = int(input("ENter num: "))

for i in range(1 , 1001):
    if i%a == 0 and i%b == 0:
        print(i)
        break
