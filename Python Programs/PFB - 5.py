import random

num = random.randint(100, 999)

a = num // 100
b = (num // 10) % 10
c = num % 10

l1 = [a, b, c]

win = 0

while win == 0:
    n = input("Enter the number: ")
    
    result = []

    n = [int(digit) for digit in n]  # Convert user input to a list of integers
    
    for i in range(3):
        if n[i] == l1[i]:
            result.append("Fermi")
        elif n[i] in l1:
            result.append("Pico")
    
    if len(result) == 0:
        result.append("Bagels")
    
    if n == l1:
        result.append("Fermi Fermi Fermi !!!")
        win = 1
    
    print(result)
