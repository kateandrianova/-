import random

i = 0
L = 5
k = 0
d = -1
x2 = ""
count = 0
m = 0
m1 = 0
maxS = ''

S = []
M = []
O = []
h = []
h1 = []

N = int(input('Введите количество шагов '))

for j in range(2**L):
    x1 = str(bin(j)[2:])
    for _ in range(0, 5 - len(x1)):
        x2 += "0"
    x2 += x1    
    S.append(x2)
    M.append((j - 2**(L-1))**2)
    x2 = ""
    
for c in range(32):
    print(c, S[c], M[c])
print()

k = random.randint(0, 31)
m = M[k]
maxS = S[k]
h.extend(S[k])

for l in range(32):
    h1.extend(S[l])
    for g in range(5):
        if h[g] != h1[g]:
            count += 1
        if count > 1:
            break
    if count == 1:
        O.append(l)
    count = 0
    h1.clear()
h.clear()

while i < N:
    print('\n')
    print('Шаг', i, maxS, m)
    print('Окрестность')
    
    for p in range(len(O)):
        print(S[O[p]], M[O[p]])
        
    for j in range(len(O)):
        if m1 < M[O[j]]:
            m1 = M[O[j]]
            d = j 
    m1 = 0
    i += 1
    
    if d == -1:
        i = N+1
    
    print('Выбранная кодировка из окрестности:', S[O[d]], M[O[d]])
    
    if m < M[O[d]]:
        m = M[O[d]]
        maxS = S[O[d]]
        h.extend(S[O[d]])
        O.clear()
        for l in range(32):
            h1.extend(S[l])
            for g in range(5):
                if h[g] != h1[g]:
                    count += 1
            if count == 1:
                O.append(l)
            count = 0
            h1.clear()
        h.clear()
        print('Смена:', maxS, m)
        print('Окрестность')
        for p in range(len(O)):
            print(S[O[p]], M[O[p]])
    else:
        i = N+1
    d = 0

print('Наилучшее решение', maxS, m)