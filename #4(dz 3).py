s = input('s: ')
list = []

while s:
    list.append(s)
    s = input('s: ')

for i in set(list):
    print(f'{i} | {list.count(i)}')
