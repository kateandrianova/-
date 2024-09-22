sumW = 0
Q = 0
a = []
summa = 0
l = 1

n = int(input('Введите количество предметов '))
s = [0 for i in range(n)]
print('Введите ценность и вес предметов')
for i in range(n):
    w = [int(i) for i in input().split()]
    summa += w[1]
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
    C = max(a)
    j = a.index(C)
    k = a[j]
    while sumW + k[1] <= w_max:
        sumW += k[1]
        Q += k[0]
        print('\nНомер шага', l, '\nВыбираемый предмет', j + 1, '\nВес', k[1], '\nЦена', k[0], '\nТекущая цена ранца', Q, '\nТекущий вес ранца', sumW)
        k[0] = 0
        s[j] = 1        
        C = max(a)
        j = a.index(C)
        k = a[j] 
        l += 1
        
print('\nИтоговое решение', *s, '\nЦенность ранца', Q, '\nОбщий вес ранца', sumW)