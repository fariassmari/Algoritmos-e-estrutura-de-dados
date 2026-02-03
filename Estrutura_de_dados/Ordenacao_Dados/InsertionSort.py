def insertionSort(tabela):
    i = 0

    for j in range(1, len(tabela)):
        aux = tabela[j]
        for i in range(j-1, -2, -1):
            if aux >= tabela[i]:
                break
            tabela[i+1] = tabela[i]
        tabela[i+1] = aux