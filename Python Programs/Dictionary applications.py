d1 = {'Nayan':5, 'Abhay':4, 'Shantanu':40, 'Anish':100}

print(d1)

print(d1.keys('5'))

print(d1.values())

d1['Avni']=100000

print(d1)

d1['Nayan']=100000

print(d1)

d2 = {'Nayan':143, 'Navin': 333, 'Kapoor': 1142}

d1.update(d2)

print(d1)

d1.pop('Nayan')

print(d1)