a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))
d = int(input('d= '))
f = int(input('f= '))
df = f - d
if not df:  
    print('Делить на 0 нельзя')
else:
    print(a * b - c / df)
