import random

class Registro:
    def __init__(self, chave=None):
        self.__chave = chave
        self.__indice = None

    @property
    def chave(self):
        return self.__chave

    @chave.setter
    def chave(self, valor):
        self.__chave = valor

    @property
    def indice(self):
        return self.__indice

    @indice.setter
    def indice(self, valor):
        self.__indice = valor

def recebe_registro(no, chave):
    r = Registro()
    r.chave = chave
    no.registro = r

class No:
    def __init__(self, registro=None):
        self.__prox = None
        self.__registro = registro

    @property
    def prox(self):
        return self.__prox

    @prox.setter
    def prox(self, valor):
        self.__prox = valor

    @property
    def registro(self):
        return self.__registro

    @registro.setter
    def registro(self, valor):
        self.__registro = valor

def imprimir_lista(tabela):
    p = tabela
    elementos = []
    while p is not None:
        elementos.append(p.registro.chave)
        p = p.prox
    print(" -> ".join(map(str, elementos)))

def busca_transposicao(chave, tabela):
    p = tabela
    q = None
    r = None
    while p != None and chave != p.registro.chave:
        r = q
        q = p
        p = p.prox
        # r -> q -> p -> p.prox(None)

    if p == None:
        return tabela, None

    if q == None: # Se q é None, p é o primeiro da lista
        return tabela, p.registro
        
    q.prox = p.prox # r -> q -> p.prox - Remove p da posição que ele parou
    p.prox = q # r -> q -> p.prox -> p - Move p para antes de q 

    if r == None:
        tabela = p # p vira o primeiro elemento da tabela
    else: 
        r.prox = p # r -> p -> q - r recebe p

    return tabela, p.registro

def busca_transposicao_rec(chave, p, q=None, r=None): 
    if p == None:
        return None, None
    
    if p.registro.chave == chave:
        if q == None:
            return p.registro, p
    
        q.prox = p.prox
        p.prox = q

        if r == None:
            return p.registro, p
        
        r.prox = p
        return p.registro, None
    return busca_transposicao_rec(chave, p.prox, p, q)

    
if __name__ == "__main__":

    # Criar lista encadeada 
    numeros = [5, 12, 7, 3, 9]
    tabela = None
    ultimo = None

    # Monta a lista
    for n in numeros:
        no = No(Registro(n))
        if tabela is None:
            tabela = no
        else:
            ultimo.prox = no
        ultimo = no

    print("\n=== Lista inicial ===")
    imprimir_lista(tabela)

    print("\n=== Testando busca TRANSPOSTA ITERATIVA ===")
    tabela, reg = busca_transposicao(9, tabela)

    if reg:
        print("Registro encontrado:", reg.chave)
    else:
        print("Chave não encontrada.")

    print("Lista após transposição (iterativa):")
    imprimir_lista(tabela)

    # --- Agora testamos a recursiva ---

    # reconstruindo a lista original para testar novamente:
    tabela2 = None
    ultimo = None
    for n in numeros:
        no = No(Registro(n))
        if tabela2 is None:
            tabela2 = no
        else:
            ultimo.prox = no
        ultimo = no

    print("\n=== Testando busca TRANSPOSTA RECURSIVA ===")
    reg, novo_inicio = busca_transposicao_rec(9, tabela2)

    if novo_inicio is not None:
        tabela2 = novo_inicio  # atualiza caso p vire primeiro

    if reg:
        print("Registro encontrado:", reg.chave)
    else:
        print("Chave não encontrada.")

    print("Lista após transposição (recursiva):")
    imprimir_lista(tabela2)