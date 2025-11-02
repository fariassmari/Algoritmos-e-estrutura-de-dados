class No:
    def __init__(self, dado = None):
        self.__dado = dado
        self.__prox = None
        self.__ant = None

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

    # get
    @property
    def ant(self):
        return self.__ant

    # set
    @ant.setter
    def ant(self, novo):
        self.__ant = novo

class Fila_Encadeada:
    def __init__(self):
        self.__inicio1 = None
        self.__inicio2 = None

    @property
    def inicio1(self):
        return self.__inicio1
    @property
    def inicio2(self):
        return self.__inicio2
    
    def esta_vazia(self):
        return self.__inicio1 == None
    
    def adicionar_tras(self, no):
        if self.__inicio1 == None:
            self.__inicio1 = no
            self.__inicio2 = no
        else:
            p = self.__inicio1
            while p.prox != None:
                p = p.prox
            p.prox = no
            no.ant = p
            self.__inicio2 = no

    def adicionar_frente(self, no):
        if self.__inicio2 == None:
            self.__inicio2 = no
            self.__inicio1 = no
        else:
            p = self.__inicio2
            while p.ant != None:
                p = p.ant
            p.ant = no
            no.prox = p
            self.__inicio1 = no
    
    def remover_frente(self):
        if self.esta_vazia() is False:
            if self.__inicio1 == self.__inicio2:
                self.__inicio1 = None
                self.__inicio2 = None
            else:
                self.__inicio1 = self.__inicio1.prox
                self.__inicio1.ant = None

    def remover_tras(self):
        if self.esta_vazia() is False:
            if self.__inicio1 == self.__inicio2:
                self.__inicio1 = None
                self.__inicio2 = None
            else:
                self.__inicio2 = self.__inicio2.ant
                self.__inicio2.prox = None
    
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
