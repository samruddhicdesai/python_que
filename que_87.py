n = 1,2,3,3,4,5,6,7

reverse = 0

while n > 0:

    digit = n % 10

    reverse = reverse * 10 + digit

    n //= 10