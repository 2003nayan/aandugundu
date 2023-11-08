arr = (input("Enter the numbers in array: "))
arr1 = arr.split()

final = [int(item) for item in arr1]

final.sort(reverse=True)

print(final)