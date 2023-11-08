import random
answer = random.randint(100,999)

a = answer//100 
b = (answer//10) - (a*10)
c = answer%10

str1 = (a,b,c)

flag = 0
while flag != 1:
    n = int(input("Enter the three digit number: "))

    x = n//100 
    y = (n//10) - (x*10)
    z = n%10

    guess = (x,y,z)

    for i in range(3):
        for guess[i] in answer and guess[i] == answer[i]:
            print("Fermi Fermi Fermi !!! ......( You Won )")
            flag = 1
            break
        for guess[i] in answer[i]:
            print("Pico...... ( Try again )")
            break
        
