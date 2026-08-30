n = int(input())
arr = list(map(int, input().split()))

unique = list(set(arr))

if len(unique) < 2:
    print(-1)
else:
    unique.sort(reverse=True)
    print(unique[1])