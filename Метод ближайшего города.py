import random

n = int(input('Введите количество городов '))
x = [i for i in range(0, n)]
s = []
r = []
z = []
i = 1
Q = 0
m = 100000

k = random.randint(0, n - 1)
s.append(x[k])
del x[k]

for j in range(n):
    a = [float(j) for j in input().split()]
    r.append(a)
    
while len(x) > 0:
    for l in range(i):
        for j in range(len(x)):
            p = r[s[l]][x[j]]
            if p != 0 and p < m:
                m = p
                g = x[j]
        if m != 1000:
            z.append((m, s[l], g))
        m = 1000
        
    Z = min(z)
    s.insert(s.index(Z[1]) + 1, Z[2])
    del x[x.index(Z[2])]
    
    print('Шаг', i)
    print('Множество кандидатов:')
    for w in range(len(z)):
        print(z[w][1], z[w][2], z[w][0])
        
    print('Выбранный город:', Z[2])
    print('Текущий обход:', *s)
    
    for w in range(len(s) - 1):
        Q += r[s[w]][s[w + 1]]
    print('Текущее растояние: ', Q)
    
    Q = 0
    i += 1
    z.clear()

print('\nИтоговый обход:', *s)

for w in range(len(s) - 1):
    Q += r[s[w]][s[w + 1]]
Q += r[s[-1]][s[0]]

print('Итоговое растояние', Q)