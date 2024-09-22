import random
sumW = 0
Q = 0
a = []
b = []
d = []
summa = 0
p_full = 0
p_full1 = 0
l = 1
p = []
o = 0

n = int(input('Введите количество предметов '))
s = [0 for i in range(n)]
print('Введите ценность и вес предметов')
for i in range(n):
    w = [int(i) for i in input().split()]
    summa += w[1]
    p_full += w[0]
    c = w[0] / w[1] 
    p_full1 += c
    b.append(c) #относительная ценность
    a.append(w[0]) #ценность
    d.append(w[1]) #вес
     
w_max = int(input('Введите общую вместимость ранца'))
    
for i in range(1, n + 1):
    print('\nНомер предмета', i, 'Цена', a[i - 1], 'Вес', d[i - 1])
    
print('\nОбщий вес ранца', summa)

if summa > w_max:
    print('\nЗадача корректная')
else:
    print('\nЗадача некорректная')
    
ans = input('Введите 1 для жадного алгоритма, 2 для алгоритма Данцига\n')
if ans == '1':  
    p.append((0, a[0]))
    o1 = 0
    o2 = a[0]
    
    for i in range(1, n):
        o1 += a[i - 1]
        o2 += a[i]
        p.append((o1, o2))
    
    if summa > w_max:
        C = random.uniform(0, p_full)
        j = -1
        while j == -1:
            for i in range(len(p)):
                if C >= p[i][0] and C <= p[i][1]:
                    j = i
        
        p[j] = (0, 0)
        while sumW + d[j] <= w_max:
            sumW += d[j]
            Q += a[j]
            print('\nНомер шага', l, '\nВыбираемый предмет', j + 1, '\nВес', d[j], '\nЦена', a[j], '\nТекущая цена ранца', Q, '\nТекущий вес ранца', sumW)
            a[j] = 0
            s[j] = 1        
            C = random.uniform(0, p_full)
            j = -1
            while j == -1:
                for i in range(len(p)):
                    if C >= p[i][0] and C <= p[i][1]:
                        j = i
                if j == -1:
                    C = random.uniform(0, p_full)
            p[j] = (0, 0)
            l += 1
             
elif ans == '2':
    p.append((0, b[0]))
    o1 = 0
    o2 = b[0]
    
    for i in range(1, n):
        o1 += b[i - 1]
        o2 += b[i]
        p.append((o1, o2))
    
    if summa > w_max:
        C = random.uniform(0, p_full1)
        j = -1
        while j == -1:
            for i in range(len(p)):
                if C >= p[i][0] and C <= p[i][1]:
                    j = i
        
        p[j] = (0, 0)
        while sumW + d[j] <= w_max:
            sumW += d[j]
            Q += a[j]
            print('\nНомер шага', l, '\nВыбираемый предмет', j + 1, '\nВес', d[j], '\nУдельная цена', b[j], '\nТекущая цена ранца', Q, '\nТекущий вес ранца', sumW)
            b[j] = 0
            s[j] = 1        
            C = random.uniform(0, p_full1)
            j = -1
            while j == -1:
                C = random.uniform(0, p_full1)
                for i in range(len(p)):
                    if C >= p[i][0] and C <= p[i][1]:
                        j = i
            p[j] = (0, 0)
            l += 1
            

print('\nИтоговое решение', *s, '\nЦенность ранца', Q, '\nОбщий вес ранца', sumW)    