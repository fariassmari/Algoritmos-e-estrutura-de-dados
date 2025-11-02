class No:
    def __init__(self, dado=None, prox=None):
        self.__dado = dado
        self.__prox = prox

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


class Pilha:
    def __init__(self, topo=None):
        self.__topo = topo

    @property
    def topo(self):
        return self.__topo
    @topo.setter
    def topo(self, valor):
        self.__topo = valor
    
    def empilhar(self, no):
        if self.__topo == None:
            self.__topo = no
        else:
            no.prox = self.__topo
            self.__topo = no

    def desempilhar(self):
        if self.__topo == None:
            self.__topo = self.__topo.prox

    def __str__(self):
        p = self.__topo
        msg = ""
        while p != None:
            msg += str(p.dado) + " "
            p = p.prox
        return msg


class ListaEncadeada:
    def __init__(self, inicio=None):
        self.__inicio = inicio

    @property
    def inicio(self):
        return self.__inicio
    @inicio.setter
    def inicio(self, valor):
        self.__inicio = valor

    def eh_vazia(self):
        return self.__inicio is None

    def inserir(self, valor):
        novo_no = No(valor)
        if self.eh_vazia():
            self.__inicio = novo_no
        else:
            atual = self.__inicio
            while atual.prox is not None:
                atual = atual.prox
            atual.prox = novo_no

    def remover(self):
        if not self.eh_vazia():
            valor = self.__inicio.dado
            self.__inicio = self.__inicio.prox
            return valor
        
    def tamanho(self):
        contador = 0
        atual = self.__inicio
        while atual is not None:
            contador += 1
            atual = atual.prox
        return contador
    
    def imprimir(self):
        atual = self.__inicio
        while atual is not None:
            print(atual.dado, end=" ")
            atual = atual.prox
        print()

# MAIN
if __name__ == '__main__':
    lista = ListaEncadeada()
    lista.inserir(10)
    lista.inserir(20)
    lista.inserir(30)
    lista.imprimir()  # Output: 10 20 30
    print("Tamanho:", lista.tamanho())  # Output: Tamanho: 3
    print("Removido:", lista.remover())  # Output: Removido: 10
    lista.imprimir()  # Output: 20 30
    print("Tamanho:", lista.tamanho())  # Output: Tamanho: 2