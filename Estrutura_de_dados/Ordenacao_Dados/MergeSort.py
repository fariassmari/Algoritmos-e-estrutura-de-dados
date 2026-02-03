def Merge(tabela, aux, iniEsq, iniDir, finalDir):
    finalEsq = iniDir - 1
    posAux = iniEsq
    nElementos = finalDir - iniEsq + 1

    while(iniEsq <= finalEsq) and (iniDir <= finalDir):
        if tabela[iniEsq] <= tabela[iniDir]:
            aux[posAux] = tabela[iniEsq]
            posAux += 1
            iniEsq += 1
        else:
            aux[posAux] = tabela[iniDir]
            posAux += 1
            iniDir += 1

    while iniEsq <= finalEsq:
        aux[posAux] = tabela[iniEsq]
        posAux += 1
        iniEsq += 1
    
    while iniDir<= finalDir:
        aux[posAux] = tabela[iniDir]
        posAux += 1
        iniDir += 1

    for i in range(nElementos):
        tabela[finalDir] = aux[finalDir]
        finalDir -= 1

def MSort(tabela, aux, esquerda, direita):
    if esquerda < direita:
        centro = (esquerda + direita) // 2
        MSort(tabela, aux, esquerda, centro)
        MSort(tabela, aux, centro+1, direita)

        Merge(tabela, aux, esquerda, centro+1, direita)

def MergeSort(tabela):
    aux = [None] * len(tabela)
    MSort(tabela, aux, 0, len(tabela)-1)
    aux = None
