dict = {1: 'One', 2: "Two", 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 0: 'Zero'}

n = int(input("Enter the number: "))

if 0 <= n < 10:
    print("It's a one digit  number.")
    print(dict[n])

elif 10 <= n < 100:
    print("It's a two digit number.")
    a = int(n/10)
    b = n%10
    print(dict[a], dict[b])

elif 100 <= n < 1000:
    print("It's a three digit number.")
    a = int(n/100)
    b = int((n%100)/10)
    c = int(n%10)
    print(dict[a], dict[b], dict[c])


elif 1000 <= n < 10000:
    print("It's a four  digit number.")
    a = int(n/1000)
    b = int((n%1000)/100)
    c = int((n%100)/10)
    d = n%10
    print(dict[a], dict[b], dict[c], dict[d])

elif 10000 <= n < 100000:
    print("It's a five digit number.")
    a = int(n/10000)
    b = int((n%10000)/1000)
    c = int((n%1000)/100)
    d = int((n%100)/10)
    e = n%10
    print(dict[a], dict[b], dict[c], dict[d], dict[e])
