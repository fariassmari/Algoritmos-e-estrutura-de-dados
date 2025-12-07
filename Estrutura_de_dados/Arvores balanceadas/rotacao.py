def rotacacao_esquerda(arvore):
    aux = arvore.dir
    arvore.dir = aux.esq
    aux.esq = arvore

    return aux
    
def rotacacao_direita(arvore):
    aux = arvore.esq
    arvore.esq = aux.dir
    aux.dir = arvore

    return aux