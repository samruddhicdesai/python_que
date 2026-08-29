def prime(n):
    if n < 2:
        return False
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
start,end = 10,80
for n in range(start,end+1):
    if prime(n):
        print(n, end=" ")