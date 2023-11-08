num = (input("Enter the number: "))

rev_num = num[::-1]

if num == rev_num:
    print("The number is palindrome.")

else:
    print("The number is not a palindrome.")