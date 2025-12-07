import random

class No:
    def __init__(self, registro, dado=None, prox=None):
        self.__dado = dado
        self.__prox = prox
        self.__registro = registro
    
    @property
    def registro(self):
        return self.__registro
    @registro.setter
    def registro(self, novo_registro):
        self.__registro = novo_registro

    @property
    def dado(self):
        return self.__dado
    @dado.setter
    def dado(self, valor):
        self.__dado = valor

    @property
    def prox(self):
        return self.__prox
    @prox.setter
    def prox(self, valor):
        self.__prox = valor

class IndiceChave:
    def __init__(self, chave=None, indice=None):
        self._chave = chave
        self._indice = indice

    @property
    def chave(self):
        return self._chave

    @chave.setter
    def chave(self, valor):
        self._chave = valor

    @property
    def indice(self):
        return self._indice

    @indice.setter
    def indice(self, valor):
        self._indice = valor

class Registro:
    def __init__(self, chave):
        self.__chave = chave
    
    @property
    def chave(self):
        return self.__chave

    @chave.setter
    def chave(self, valor):
        self._chave = valor

def imprimir_lista(tabela):
    p = tabela
    elementos = []
    while p is not None:
        elementos.append(p.registro.chave)
        p = p.prox
    print(" -> ".join(map(str, elementos)))

def busca_indexada(chave, indices, tabela):
    i = 0
    while i < len(indices):
        if indices[i].chave > chave:
            break
        i += 1
        
    if i == 0:
        inferior = 0
    else:
        inferior = indices[i-1].indice
        
    if i == len(indices):
        superior = len(tabela) - 1
    else: 
        superior = indices[i].indice - 1

    result = -1

    for j in range(inferior, superior+1):
        if tabela[j].chave == chave:
            result = j
            break

    return result

def busca_indexada_rec(chave, indices, tabela, i=0, inferior=None, superior=None, j=None):
    if inferior == None:
        if i == len(indices):
            inferior = indices[-1].indice
            superior = len(tabela) - 1
            return inferior, superior
        elif indices[i].chave > chave:
            if i == 0:
                inferior = 0 
                superior = indices[0].indice - 1
            else:
                inferior = indices[i-1].indice
                superior = indices[i].indice - 1
                return inferior, superior
        else:
            return busca_indexada_rec(chave, indices,tabela, i+1)

        j = inferior
    
    if j > superior:
        return -1
    elif tabela[j].chave == chave:
        return j
    else:
        return busca_indexada_rec(chave, indices, tabela, i, inferior, superior, j + 1)


if __name__ == "__main__":

    # Cria tabela principal ORDENADA
    tabela = [
        Registro(100),
        Registro(150),
        Registro(200),
        Registro(250),
        Registro(300),
        Registro(350),
        Registro(400),
        Registro(450),
        Registro(500)
    ]

    # Criação da tabela de índices (elementos 0, 3, 6...)
    indices = [
        IndiceChave(tabela[0].chave, 0),
        IndiceChave(tabela[3].chave, 3),
        IndiceChave(tabela[6].chave, 6)
    ]

    print("\n=== TABELA PRINCIPAL ===")
    print([reg.chave for reg in tabela])

    print("\n=== TABELA DE ÍNDICES ===")
    for idx in indices:
        print(f"Chave = {idx.chave}, Índice = {idx.indice}")

    # Teste de busca
    chave_busca = 350

    pos = busca_indexada(chave_busca, indices, tabela)

    if pos != -1:
        print(f"Chave encontrada na posição {pos} da tabela.")
    else:
        print("Chave NÃO encontrada.")