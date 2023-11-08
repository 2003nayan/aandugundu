str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

a = len(str1)
b = len(str2)

if a != b:
    print("The strings aren't anagrams. ")

else:

    count1 = {}
    count2 = {}

    for char in str1:
        count1[char] = count1.get(char,0) + 1

    for char in str2:
        count2[char] = count2.get(char,0) + 1

    if count1==count2:
        print("The strings are anagrams.")

    else:
        print("The strings are not anagrams. ")