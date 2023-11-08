import math

num = int(input("Enter a positive integer: "))

if num <= 1:
    print("Not a prime number.")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("It is a prime number.")
    else:
        print("Not a prime number.")
