import random

# num=str(random.randint(0,999))
num=''
li = ['0','1','2','3','4','5','6','7','8','9']
random.shuffle(li)
for i in li[:3]:
    num+=i
    
num

# num="123"
win=1
while win!=0:
    
    guess=input("enter guess:")
    
    result = []


    for i in range(3):
        if guess[i] in num and guess[i]==num[i] :
            result.append('fermi')

        elif guess[i]in num:
            result.append('pico')



    if len(result)==0:
        result.append("bagels")
        print(result)
    elif guess==num:
        result.append("FERMI FERMI FERMI !!!")
        print(result)
        win=0
    else:
        random.shuffle(result)
        print(result)