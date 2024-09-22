import random

n = int(input('Введите количество городов '))
x = [i for i in range(1, n + 1)]
s = []
r = []
i = 1
summa = 0
m = 100000

k = random.randint(0, n - 1)
f = x[k] - 1
s.append(x[k])
del x[k]


for j in range(n):
    a = [float(j) for j in input().split()]
    r.append(a)
    

while len(x) > 0:
    for l in range(len(x)):
        j = r[f][x[l] - 1]
        if j < m and j != 0:
            m = j
            g = l
    s.append(x[g])
    summa += m
    print('\nШаг:', i, '\nТекущий обход:', *s, '\nВыбранный город:', x[g], '\nРасстояние до выбранного города:', r[f][x[g] - 1], '\nДлина текущего обхода:', summa)
    f = x[g] - 1
    del x[g]
    m = 10000
    i += 1
    
summa += r[s[-1] - 1][s[0] - 1]
print('\nИтоговый цикл', *s, '\nПолученная длина', summa)