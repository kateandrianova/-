import random
import math

i = 0
L = 7
m = 0
k = 0
w = 0
d = -1
m1 = 0
count = 0
maxS = ''
x1 = ''
x2 = ''

S = []
M1 = []
O = []
h = []
h1 = []

N = int(input('Введите глубину поиска '))
M = int(input('Введите число стартов '))

for j in range(1, 2**L):
    x1 = str(bin(j)[2:])
    for _ in range(0, L - len(x1)):
        x2 += '0'
    x2 += x1    
    S.append(x2)
    M1.append(5*math.sin(j) + math.log(j))
    x2 = ''

for c in range(32):
    print(c, S[c], M1[c])
print()

k = random.randint(0, 127)
m = M1[k]
maxS = S[k]

while w < M:
    O.clear()
    h.extend(maxS)
    for j in range(2**L - 1):
        h1.extend(S[j])
        for g in range(L):
            if h[g] != h1[g]:
                count += 1
            if count > 1:
                break
        if count == 1:
            O.append(j)
        count = 0
        h1.clear()
    h.clear()
    print()
    k = random.randint(0, 2)
    
    if k == 0: #Монте-Карло
        print('Монте-Карло')
        while i < N:
            print('Шаг', i, '  max:', m, '  maxS:', maxS, '  s:', S[i])
            p = random.randint(0, 2**L - 1)
            print('Выбранная кодировка', S[p], M1[p])
            if m < M1[p]:
                m = M1[p]
                maxS = S[p]
                print('Смена:', '  max:', m, '  maxS:', maxS)
            i += 1
        w += 1
        i = 0
        print('Наилучшее решение после алгоритма', maxS, m)
        
    elif k == 1: #Холм в глубину
        print('Холм в глубину')
        while i < N:                  
            if len(O) > 0:
                print('Шаг', i, maxS, m)
                print('Окрестность')
                for p in range(len(O)):
                    print(S[O[p]], M1[O[p]])
                   
                i += 1
                k = random.choice(O)
                print('Выбранная кодировка из окрестности:', S[k], M1[k])
                if m < M1[k]:
                    maxS = S[k]
                    m = M1[k]
                    h.extend(S[k])
                    O.clear()
                    for l in range(2**L - 1):
                        h1.extend(S[l])
                        for g in range(L):
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
                        print(S[O[p]], M1[O[p]])
                else:
                    del O[O.index(k)]
            else:
                break
        w += 1
        i = 0
        print('Наилучшее решение после алгоритма', maxS, m)  
        
    else: #Холм в ширину
        print('Холм в ширину')
        while i < N:      
            print('Шаг', i, maxS, m)
            print('Окрестность')
            
            for p in range(len(O)):
                print(S[O[p]], M1[O[p]])
                
            for j in range(len(O)):
                if m1 < M1[O[j]]:
                    m1 = M1[O[j]]
                    d = j 
            m1 = 0
            i += 1
            
            if d == -1:
                i = N+1
            
            print('Выбранная кодировка из окрестности:', S[O[d]], M1[O[d]])
            
            if m < M1[O[d]]:
                m = M1[O[d]]
                maxS = S[O[d]]
                h.extend(S[O[d]])
                O.clear()
                for l in range(2**L - 1):
                    h1.extend(S[l])
                    for g in range(L):
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
                    print(S[O[p]], M1[O[p]])
            else:
                i = N+1
            d = 0                  
        w += 1
        i = 0
        print('Наилучшее решение после алгоритма:', maxS, m)