numbers = [1,2,3,4,2]

seen = set()

for n in numbers:
    if n in seen:
        print("Dulicate:",n)
        break

    seen.add(n)