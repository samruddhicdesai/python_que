string = input("Enter string: ")
frequency = {}
for ch in string:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
print(frequency)