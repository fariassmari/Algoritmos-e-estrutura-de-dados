import random

def busca_binaria(chaves, chave_procurada):
    inf = 0
    sup = 0
    while inf <= sup:
        meio = (inf + sup)//2
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
        meio = (inf + sup)//2

        if chaves[meio] == chave_procurada:
            return meio
        elif chaves[meio] < chave_procurada:
            return busca_binaria_rec(chaves, chave_procurada, meio + 1, sup)
        else:
            return busca_binaria_rec(chaves, chave_procurada, inf, sup - 1)
    return -1

# Gera um número inteiro aleatório entre 1 e 100 (inclusive)
chaves = []

for i in range(1,10):
  chaves.append(random.randint(1, 15))

print(chaves)

chave_procurada = 2
indice = busca_binaria_rec(chaves, chave_procurada, 0, len(chaves)-1)

print(indice)