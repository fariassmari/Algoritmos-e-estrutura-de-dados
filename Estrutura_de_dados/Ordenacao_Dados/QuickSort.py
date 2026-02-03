def particiona(tabela, inf, sup):
    pivo = tabela[inf]
    sobe = inf
    desce = sup

    while sobe > desce:
        while tabela[sobe] <= pivo and sobe < sup:
            sobe += 1
        while tabela[desce] > pivo:
            desce -= 1

        if sobe < desce:
            tabela[desce], tabela[sobe] = tabela[sobe], tabela[desce] 

    tabela[inf], tabela[desce] = tabela[desce], pivo

    return desce

def quick(tabela, inf, sup):
    if inf < sup:
        posPivo = particiona(tabela, inf, sup)
        quick(tabela, inf, posPivo-1)
        quick(tabela, posPivo+1, sup)

def quickSort(tabela):
    quick(tabela, 0, len(tabela)-1)