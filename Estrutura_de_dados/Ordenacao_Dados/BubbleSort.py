def bubbleSort(tabela):
    n = len(tabela)

    for i in range(n):
        for j in range(0, n-1):
            if tabela[j] > tabela[j+1]:
                tabela[j], tabela[j+1] = tabela[j+1], tabela[j]

def bubbleSort_melhor(tabela):
    ordenado = 0
    while not ordenado:
        ordenado = 1
        for i in range(len(tabela) - 1):
            if tabela[i] > tabela[i+1]:
                ordenado = 0
                tabela[i], tabela[i+1] = tabela[i+1], tabela[i]