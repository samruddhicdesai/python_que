number = [1,2,3,4,5,6,5,443,2,3]
result = list(set(filter(lambda x : x % 2== 0,number)))
print(list(result))