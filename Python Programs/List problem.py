a = (input("Enter the elements in the first list: "))
list_1 = [int(x) for x in a.split()]

b = (input("Enter the elements in the second list: "))
list_2 = [int(x) for x in b.split()]

m = len(list_1)
n = len(list_2)

total_in_first = 0
total_in_second = 0

for i in range(0,m):
    l1 = list_1[i]*(10**i)
    total_in_first += l1
'print(total_in_first)'

for i in range(0,n):
    l2 = list_2[i]*(10**i)
    total_in_second += l2
'print(total_in_second)'

print("Total sum is: ", total_in_first + total_in_first)