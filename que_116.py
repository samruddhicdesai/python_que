list = list(map(int , input().split()))
freq = {}
for num in list:
    freq[num] = freq.get(num,0)+1
print(freq)