def s(n):
    sezoni = {
        2 < n < 6: 'Весна',
        5 < n < 9: 'Лето',
        8 < n < 12: 'Осень',
        n == 12 or n < 3: 'Зима',
    }
    return sezoni[True]

m = int(input('Месяц: '))
print(s(m))
