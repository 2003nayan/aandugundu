dict = {1: 'One', 2: "Two", 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Fourty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',90: 'Ninety', 100: 'One Hundred', 200: 'Two Hundred', 300: 'Three Hundred', 400: 'Four Hundred', 500: 'Five hundred', 600: 'Six hundred', 700: 'Seven Hundred', 800: 'Eight hundred', 900: 'Nine Hundred', 1000: 'One Thousand', 2000: 'Two Thousand', 3000: 'Three Thousand', 4000: 'Four Thousand', 5000: 'Five Thousand', 6000: 'Six thousand', 7000: 'Seven Thousand', 8000: 'Eight Thousand', 9000: 'Nine Thousand'}

n = int(input("Enter the number: "))

if 0 <= n < 10:
    print("It's a one digit  number.")
    print(dict[n])

elif 10 <= n < 100:
    print("It's a two digit number.")
    a = (int(n/10))*10
    b = n%10
    print(dict[a], dict[b])

elif 100 <= n < 1000:
    print("It's a three digit number.")
    a = int(n/100)*100
    b = int((n%100)/10)*10
    c = int(n%10)
    print(dict[a], dict[b], dict[c])


elif 1000 <= n < 10000:
    print("It's a four  digit number.")
    a = int(n/1000)*1000
    b = int((n%1000)/100)*100
    c = int((n%100)/10)*10
    d = n%10
    print(dict[a], dict[b], dict[c], dict[d])

