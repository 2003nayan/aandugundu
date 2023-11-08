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
        for y in l1:
            for z in l1:
                if x == a and y == b and z == c:
                    print("Fermi Fermi Fermi !!!")
                elif (x != a and y == b and z == c) or (x == a and y != b and z == c) or (x == a and y == b and z != c):
                    print("Fermi Pico")
                elif (x != a and y != b and z == c) or (x == a and y != b and z != c) or (x != a and y == b and z != c):
                    print("Fermi Pico Pico")
                elif (x != a and y != b and z != c):
                    print("Pico Pico Pico")
                break

            if z not in l1:
                if x == a and y == b:
                    print("Fermi Fermi")
                    if (x != a and y == b) or (x == a and y != b):
                        print("Fermi Pico")
                    elif (x != a and y != b):
                        print("Pico Pico")
            break

        if y not in l1:
            for z in l1:
                if x == a and z == c:
                    print("Fermi Fermi")
                elif (x != a and z == c) or (x == a and z != c):
                    print("Fermi Pico")
                elif (x != a and z != c):
                    print("Pico Pico")

            if z not in l1:
                if y == b:
                    print("Fermi")
                else: 
                    print("Pico") 
        break

    if x not in l1:
        for y in l1:
            for z in l1:
                if y == b and z == c:
                    print("Fermi Fermi")
                elif (y != b and z == c) or (y == b and z != c):
                    print("Fermi Pico")
                elif (y != b and z != c):
                    print("Pico Pico")

            if z not in l1:
                if y == b:
                    print("Fermi")
                else: 
                    print("Pico")  

        if y not in l1:
            for z in l1:
                if z == c:
                    print("Fermi")
                else: 
                    print("Pico")

    if x not in l1 and y not in l1 and z not in l1:
        print("Bagels")           