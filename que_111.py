string = input("enter any string: ")
result = ""
for ch in string:
    if ch not in result:
        result += ch
    
print(result)