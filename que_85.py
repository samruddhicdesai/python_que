numbers = [1,2,3,4,5,6,1,2,3,4,5]
frequency = {}

for n in numbers:

    if n in frequency:
        frequency[n] += 1
    else:
        frequency[n] = 1

print(frequency)