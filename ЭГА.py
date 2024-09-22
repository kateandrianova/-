import random

n = 15
k = 15
c = [11, 18, 23, 21, 23, 30, 23, 3, 4, 6, 24, 2, 10, 15, 6]
w = [1, 25, 29, 24, 27, 21, 24, 13, 16, 15, 23, 14, 15, 3, 16]
s = [0 for i in range(n)]
r = []
Q = []
count_generation = 1

Wmax = 106
summa = 0
q = 0

ans1 = input('Выберите способ формирования начальной популяции \n1 - Случайно с контролем  \n2 - Эвристика\n')
ans2 = input('Выберите кроссовер \n1 - Одноточечный  \n2 - Двухточечный \n3 - Однородный\n')
ans3 = input('Выберите мутацию \n1 - Генная \n2 - Сальтация\n3 - Хромосомная\n')
ans4 = input('Выберите стратегию формирования \n1 - Поколенческая \n2 - Устойчивое состояние\n')

if ans1 == '1':
    for j in range(k):
        for i in range(n):
            x = random.randint(0, 1)
            if x == 1:
                if summa + x*w[i] < Wmax:
                    summa += x*w[i]
                    q += c[i]
                    s[i] = 1
        r.append(s)
        Q.append(q)
        s = [0 for i in range(n)]
        summa = 0
        q = 0
        
        
elif ans1 == '2':
    p1 = []
    p1.append((0, c[0]))
    o1 = 0
    o2 = c[0]
    p_full = c[0]
    
    for i in range(1, n):
        p_full += c[i]
        o1 += c[i - 1]
        o2 += c[i]
        p1.append((o1, o2))    
        
    for i in range(k):
        p = p1.copy()
        C = random.randint(0, p_full)
        j = -1
        while j == -1:
            for l in range(len(p)):
                if C >= p[l][0] and C <= p[l][1]:
                    j = l
                    break
        
        p[j] = (0, 0)
        while summa + w[j] <= Wmax:
            summa += w[j]
            q += c[j]
            s[j] = 1      
            j = -1
            while j == -1:
                C = random.randint(0, p_full)
                for l in range(len(p)):
                    if C >= p[l][0] and C <= p[l][1]:
                        j = l
                        break  
            p[j] = (0, 0)
        summa = 0
        r.append(s)
        Q.append(q)
        s = [0 for i in range(n)]
        q = 0
        
print('Начальная популяция:')
for i in range(k):
    print(*r[i], Q[i])

while len(r) != 0:
    generation = []
    mutation = []    
    #print('\nВыбор родительской пары')
    sum_Q = 0
    parents = [] 
    for i in range(k):
        sum_Q += Q[i]
        
    m1 = 0
    i1 = 0
    for i in range(k//2 + 1):
        for m in range(len(Q)):
            p1 = Q[m] / sum_Q
            if p1 > m1:
                m1 = p1
                i1 = i            
        parents.append(r[i1])
        Q[i1] = 0
        m1 = 0
                          
    '''for i in range(len(parents)):
        print(*parents[i])'''
    
    #print('Кроссовер')
    child = [0 for i in range(n)]
    kids = []
    if ans2 == '1':
        for j in range(k):
            parent1 = random.choice(parents) 
            for i in range(n//2):
                child[i] = parent1[i]
            parent2 = random.choice(parents)
            while parent2 == parent1:
                parent2 = random.choice(parents)
            for i in range(n//2, n):
                child[i] = parent2[i]
            kids.append(child)
            mutation.append(child)
            child = [0 for i in range(n)]
            
    elif ans2 == '2':
        break1 = random.randint(0, n //2)
        break2 = random.randint(n // 2 + 1, n - 1)
        for j in range(k):
            parent1 = random.choice(parents) 
            for i in range(break1):
                child[i] = parent1[i]
            parent2 = random.choice(parents)
            while parent2 == parent1:
                parent2 = random.choice(parents)
            for i in range(break1, break2):
                child[i] = parent2[i]
                
            e = random.randint(0, 1)
            if e == 1:
                parent3 = parent1
            else:
                parent3 = parent2
            for i in range(break2, n):
                child[i] = parent3[i]   
                
            kids.append(child)
            mutation.append(child)
            child = [0 for i in range(n)]  
            
    elif ans2 == '3':
        for j in range(k):
            parent1 = random.choice(parents) 
            parent2 = random.choice(parents)
            while parent2 == parent1:
                parent2 = random.choice(parents)            
            for i in range(n):
                y = random.randint(0, 1)
                if y == 1:    
                    child[i] = parent1[i]
                else:
                    child[i] = parent2[i]
                    
            kids.append(child)
            mutation.append(child)
            child = [0 for i in range(n)]
        
    #print(*kids, sep = '\n')
    
    #print('Мутация')
    if ans3 == '1':
        for i in range(k):
            y = random.randint(0, n - 1)
            if mutation[i][y] == 0:
                mutation[i][y] = 1
            else:
                mutation[i][y] = 0    
    elif ans3 == '2':
        for i in range(k):
            for j in range(4):
                y = random.randint(0, n - 1)
                if mutation[i][y] == 0:
                    mutation[i][y] = 1
                else:
                    mutation[i][y] = 0   
    elif ans3 == '3':
        for i in range(k):
            for j in range(n):
                if mutation[i][j] == 0:
                    mutation[i][j] = 1
                else:
                    mutation[i][j] = 0    
                    
    #print(*mutation, sep = '\n')  
    generation1 = []
    for i in range(len(mutation)):
        generation1.append(mutation[i])
        generation1.append(kids[i])
        
    if ans4 == '1':
        generation = generation1.copy()
    elif ans4 == '2':
        G = round(random.random() * 2 * k)
        for i in range(G):
            j = random.randint(0, 2 * k - 1)
            generation.append(generation1[j])
        for i in range(k - G):
            j = random.randint(0, k // 2)
            generation.append(parents[j])
        
    #print('Селекция')
    fitness = []
    w1 = []
    weight = []
    price = []
    selection = []
    for l in range(len(generation)):
        one = generation[l]
        f = 0
        d = 0
        for v in range(len(one)):
            f += one[v]*c[v]
            d += one[v]*w[v]
        fitness.append(f)
        w1.append(d)
        
    roulette = []
    roulette.append((0, fitness[0]))
    o1 = 0
    o2 = fitness[0]
    full = fitness[0]
    
    for i in range(1, len(fitness)):
        full += fitness[i]
        o1 += fitness[i - 1]
        o2 += fitness[i]
        roulette.append((o1, o2))
        
    for l in range(k + 2):
        C = random.randint(0, full)
        j = -1
        while j == -1:
            C = random.randint(0, full)
            for i in range(len(roulette)):
                if C >= roulette[i][0] and C <= roulette[i][1]:
                    j = i
                    break
        roulette[j] = (0, 0)
        selection.append(generation[j])
        price.append(fitness[j])
        weight.append(w1[j])
        
    #print(*selection, sep = '\n')    
    
    #print('\nДекодер')#модификация генотипа
    modification = []
    count = 0
    for i in range(len(selection)):
        one = selection[i]
        if weight[i] > Wmax:
            for j in range(len(one)):
                while weight[i] > Wmax:
                    l = random.randint(0, n - 1)
                    if one[l] == 1:
                        selection[i][l] = 0
                        weight[i] -= w[l]
                break
        modification.append(selection[i])
    k1 = 0    
    r = modification
    k = len(modification)
    Q.clear()
    for i in range(len(modification)):
        q1 = 0
        one = modification[i]
        for j in range(len(one)):
            q1 += one[j]*c[j]
        Q.append(q1)
    if len(Q) != 0:
        q_max = max(Q)
        j = Q.index(q_max)
        print('\n\n\n', count_generation)
        count_generation += 1        
        print('Наилучшая особь', modification[j], Q[j])
        best = modification[j]
        m_best = Q[j]
        print('Популяция')
        for i in range(len(modification)):
            print(modification[i], Q[i])  
            
    for i in range(k):
        for j in range(i, k):
            if price[i] == price[j] and i != j:
                k1 += 1
    if k1 > k*0.6:
        break    
print('\n\nНаилучшая особь:', best, m_best)


