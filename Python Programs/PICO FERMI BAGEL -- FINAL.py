import random

num = random.randint(100, 999)

a = num//100
b = num//10 - a*10
c = num%10

l1 = [a,b,c]

win = 0

while win == 0:
    n = input("Enter the guessed number: ")
    l2 = [int(digit) for digit in n]

    result = []

    for i in range(3):
        if l2[i] == l1[i]:
            result.append("Fermi")


        elif l2[i] in l1:
            result.append("Pico")

        
    if len(result) == 0:
        result.append("Bagels")

    if l2 == l1:
        result.append("Fermi Fermi Fermi !!!")
        win = 1

    print(result)