str1 = input("Enter the string to check if it's palindrome: ")

str2 = str1[::-1]

if str2 == str1:
    print("The string is palindrome. ")

else:
    print("The string is not a palindrome. ")    