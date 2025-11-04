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

    def __str__(self):
        return str(self.dado) 

class Pilha_Encadeada:
    def __init__(self):
        self.__topo = None

    @property
    def topo(self):
        return self.__topo

    def esta_vazia(self):
        return self.__topo is None

    def empilhar(self, no):
        no.prox = self.__topo
        self.__topo = no
    
    def desempilhar(self):
        if self.__topo is not None:
            no = self.__topo
            self.__topo = self.__topo.prox
            return no
        
    def trocar(self, valor, novo_valor):
        if self.__topo != None:
            p = self.__topo
            while p != None:
                if p.dado == valor:
                    p.dado = novo_valor
                p = p.prox
        
    
    def __str__(self):
        saida = '['
        p = self.__topo
        while p != None:
            saida += f'{p.dado}'
            p = p.prox
            if p != None:
                saida += ', '
        saida += ']'
        return saida

if __name__ == '__main__':

    p = Pilha_Encadeada()

    p.empilhar(No("A"))
    p.empilhar(No("B"))
    p.empilhar(No("C"))
    p.empilhar(No("D"))

    print(p)

    p.trocar("A", "B")
    print(p)

    p.desempilhar()
    print(p)

    p.desempilhar()
    print(p)


