word = "madamm"

reverse = ""

for char in word:
    reverse = char + reverse
if word == reverse:
        print("Palindrome")
else:
      print("Not palindrome")