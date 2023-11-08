import math

num = input("Enter the number: ")

num = int(num)

for i in range(2, int((math.sqrt(num))) +1):
    if num%i==0:
        print ("The number is not a prime number.")

    else:
        print("The number is a prime number.")    

