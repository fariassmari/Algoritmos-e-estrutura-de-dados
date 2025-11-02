class No:
    def __init__(self, dado = None):
        self.__dado = dado
        self.__prox = None

    # get
    @property
    def dado(self):
        return self.__dado

    # set
    @dado.setter
    def dado(self, novo):
        self.__dado = novo

    # get
    @property
    def prox(self):
        return self.__prox

    # set
    @prox.setter
    def prox(self, novo):
        self.__prox = novo

class Fila_Encadeada:
    def __init__(self):
        self.__inicio = None
        self.__fim = None

    @property
    def inicio(self):
        return self.__inicio

    @property
    def fim(self):
        return self.__fim
    
    def esta_vazia(self):
        return self.__inicio == None
    
    def adicionar(self, no):
        if self.__inicio == None:
            self.__inicio = no
        else:
            p = self.__inicio
            while p.prox != None:
                p = p.prox
            p.prox = no

    
    def remover(self):
        if self.esta_vazia() is False:
            self.__inicio = self.__inicio.prox
    
    def size(self):
        p = self.__inicio
        tamanho = 0
        while p != None:
            tamanho += 1
            p = p.prox
        return tamanho
    
    def __str__(self):
        saida = '['
        p = self.__inicio
        while p != None:
            saida += f'{p.dado}'
            p = p.prox
            if p != None:
                saida += ', '
        saida += ']'
        return saida
    
if __name__ == '__main__':

    p = Fila_Encadeada()

    p.adicionar(No("A"))
    p.adicionar(No("B"))
    p.adicionar(No("C"))
    p.adicionar(No("D"))

    print(p)
    print(p.size())

    p.remover()
    print(p)
    print(p.size())

    p.remover()
    print(p)
    print(p.size())

    p.remover()
    print(p)
    print(p.size())

    p.remover()
    print(p)
    print(p.size())
