import random
answer = random.randint(100,999)

a = answer//100 
b = (answer//10) - (a*10)
c = answer%10

l1 = [a,b,c]

n = 0
while n != answer:
    n = int(input("Enter the number: "))
    x = n // 100
    y = (n // 10) % 10
    z = n % 10

    l2 = [x,y,z]

    for x in l1:
        for i in range(0,3):
            if x == l1[0]:
                