import math

num = int(input("Enter the number: "))

Divisor_sum = 0

for i in range(1, num-1):
    if num%i==0:
        Divisor_sum += i

if Divisor_sum==num:
    print ("Yes, the number is a perfect number.")

else:
    print("No, the number isn't a perfect number.")    