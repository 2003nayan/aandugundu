arr1 = input("Enter elements of the array separated by spaces: ")
arr2 = arr1.split()
final_array = [int(item) for item in arr2]

sorted_array = sorted(final_array)
print("Input array:", sorted_array)
