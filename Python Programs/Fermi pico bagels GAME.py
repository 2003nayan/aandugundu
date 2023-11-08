import random
answer = random.randint(100,999)

a = answer//100 
b = (answer//10) - (a*10)
c = answer%10

l1 = [a,b,c]

n = int(input("Enter the number: "))
while n != answer:
    
    x = n // 100
    y = (n // 10) % 10
    z = n % 10

    l2 = [x,y,z]

    if x == a:
        if y == b:
            if z == c:
                print("Fermi Fermi Fermi !!!")
            else:
                print("Fermi Fermi")
        elif y == c: 
            print("Fermi Pico")
        else:
            print("Fermi")
    elif x == b or x == c:
            if y == b:
                if z == c:
                    print("Fermi Pico")
                elif z == a or z == b:
                    print("Fermi Pico Pico")
                else:
                    print("Fermi Pico")
            elif y == a or y == c:
                if z == c:
                    print("Fermi Pico Pico")
                elif z == 