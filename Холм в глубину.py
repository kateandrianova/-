import random

i = 0
L = 5
k = 0
x2 = ""
count = 0
m = 0
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
    M.append(j)
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
    if len(O) > 0:
        print('\n')
        print('Шаг', i, maxS, m)
        print('Окрестность')
        for p in range(len(O)):
            print(S[O[p]], M[O[p]])
           
        i += 1
        k = random.choice(O)
        print('Выбранная кодировка из окрестности:', S[k], M[k])
        if m < M[k]:
            maxS = S[k]
            m = M[k]
            h.extend(S[k])
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
            del O[O.index(k)]
    else:
        break

print()
print('Наилучшее решение:', maxS, m)