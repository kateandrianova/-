sumW = 0
Q = 0
a = []
b = []
summa = 0
l = 1

n = int(input('Введите количество предметов '))
s = [0 for i in range(n)]
print('Введите ценность и вес предметов')
for i in range(n):
    w = [int(i) for i in input().split()]
    summa += w[1]
    c = w[0] / w[1] 
    b.append(c)
    a.append(w)
    
print('Введите максимальный вес ранца')   
w_max = int(input())

for i in range(1, n + 1):
    w = a[i - 1]
    print('\nНомер предмета', i, 'Цена', w[0], 'Вес', w[1])
    
print('\nОбщий вес ранца', summa)

if summa > w_max:
    print('\nЗадача корректная')
else:
    print('\nЗадача некорректная')

if summa > w_max:
    B = max(b)
    j = b.index(B)
    k = a[j]
    while sumW + k[1] <= w_max:
        sumW += k[1]
        Q += k[0]
        print('\nНомер шага', l, '\nВыбираемый предмет', j + 1, '\nОтносительный вес', B, '\nЦена', k[1], '\nТекущая цена ранца', Q, '\nТекущий вес ранца', sumW)
        b[j] = 0
        s[j] = 1        
        B = max(b)
        j = b.index(B)
        k = a[j] 
        l += 1
        
print('\nИтоговое решение', *s, '\nЦенность ранца', Q, '\nОбщий вес ранца', sumW)