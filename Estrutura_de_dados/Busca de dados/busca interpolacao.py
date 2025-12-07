import random

def busca_binaria(chaves, chave_procurada):
    inf = 0
    sup = len(chaves) - 1
    meio = 0
    while inf <= sup:
        meio = inf + int((sup - inf) * ((chave_procurada - chaves[inf]) / (chaves[sup] - chaves[inf])))
        if chaves[meio] == chave_procurada:
            return meio
        elif chaves[meio] > chave_procurada:
            sup = meio -1
        else:
            inf = meio + 1
    return -1

# Recursiva
def busca_binaria_rec(chaves, chave_procurada, inf, sup):
    if inf <= sup:
        meio = inf + (sup - inf) * ((chave_procurada - chaves[inf]) / (chaves[sup] - chaves[inf]))

        meio = int(meio)

        if chaves[meio] == chave_procurada:
            return meio
        elif chaves[meio] < chave_procurada:
            return busca_binaria_rec(chaves, chave_procurada, meio + 1, sup)
        else:
            return busca_binaria_rec(chaves, chave_procurada, inf, sup - 1)
    return -1

# Gera um número inteiro aleatório entre 1 e 100 (inclusive)
chaves = [5,10,15,20,25,30,35,40,45,50,55,60,65,70]

chave_procurada = 20
indice = busca_binaria_rec(chaves, chave_procurada, 0, len(chaves)-1)

print(indice)