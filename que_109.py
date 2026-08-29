string = input("Enter string: ").lower()

vowels = "aeiou"
v = 0
consonants = 0

for ch in string:
    if ch in vowels:
        v += 1
    elif ch.isalpha():
        consonants += 1

print("Vowels:", v)
print("Consonants:", consonants)