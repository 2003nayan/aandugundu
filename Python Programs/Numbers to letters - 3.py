dict = {1: 'One', 2: "Two", 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
    10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
    17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
    60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 0: ' '}


n = int(input("Enter the number: "))

if 0 <= n < 10:
    print("It's a one digit  number.")
    print(dict[n])

elif 10 <= n < 100:
    print("It's a two digit number.")
    if 10 < n < 20:
        print(dict[n])
    else:
        a = (n//10)*10
        b = n%10
        print(dict[a], dict[b])

elif 100 <= n < 1000:
    print("It's a three digit number.")
    a = (n//100)
    if 10 < n%100 < 20:
        b = n%100
        c = 0
    else:
        b = ((n%100)//10)*10
        c = (n%10)
    print(dict[a], " hundred ", dict[b], dict[c])


elif 1000 <= n < 10000:
    print("It's a four  digit number.")
    a = (n//1000)
    b = ((n%1000)//100)
    if 10 < n%100 < 20:
        c = n%100
        d = 0
    else:
        c = ((n%100)//10)*10
        d = n%10
    if  b==0:
        print(dict[a], " Thousand ", dict[b], dict[c], dict[d])
    else:
        print(dict[a], " Thousand ", dict[b], " Hundred " ,dict[c], dict[d])