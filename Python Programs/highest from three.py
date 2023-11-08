num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if (num1>num2):
    
    if (num1>num3):
        print("The highest number is first number: ", num1 )

    if (num3>num1):
        print("The highest number is third number: ", num3)

if(num2>num1):
    if(num2>num3):
        print("The highest number is second number: ", num2)   

    if (num3>num2):
        print("The highest number is third number: ", num3)
