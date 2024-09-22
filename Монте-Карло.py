import random

i = 0
m = 0
maxS = ''
L = 15

S = []
M = []

N = int(input('Введите количество шагов '))

for j in range(2**L):
    x = random.randint(0, 2**L)
    S.append(bin(x)[2:])
    M.append(random.randint(1, 100))
    
for k in range(32):
    print(S[k], M[k], sep = '  ')

print()

while i < N:
    print('Шаг', i, '  max:', m, '  maxS:', maxS, '  s:', S[i])
    if m < M[i]:
        m = M[i]
        maxS = S[i]
        print('Смена:', '  max:', m, '  maxS:', maxS)
    i += 1

print('Ответ', maxS, m)