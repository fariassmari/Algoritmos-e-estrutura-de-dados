class No:
    def __init__(self, dado = None):
        self.__dado = dado
        self.__dir = None
        self.__esq = None

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
    def dir(self):
        return self.__dir

    # set
    @dir.setter
    def dir(self, novo):
        self.__dir = novo

    # get
    @property
    def esq(self):
        return self.__esq

    # set
    @esq.setter
    def esq(self, novo):
        self.__esq = novo

class Arvore_Binaria:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, novo_root):
        self.__root = novo_root

    def pre_ordem(self, no):
        print(no.dado)
        self.pre_ordem(no.esq)
        self.pre_ordem(no.dir)

    def ordem(self, no):
        self.ordem(no.esq)
        print(no.dado)
        self.ordem(no.dir)

    def pos_ordem(self, no):
        self.pos_ordem(no.esq)
        self.pos_ordem(no.dir)
        print(no.dado)

    def nos(self, no):
        if no != None:
            return 1 + self.nos(no.esq) + self.nos(no.dir)
        else:
            return 0
        
    def nos_folhas(self, no):
        if no.esq == None and no.dir == None:
            return 1 
        else:
            return self.nos_folhas(no.esq) + self.nos_folhas(no.dir)

    def busca_valor(self, no, valor):
        if no != None:
            if no.dado == valor:
                return True
            else:
                return self.busca_valor(no.esq, valor) or self.busca_valor(no.dir, valor)
        else:
            return False

    def busca_valor1(self, no, valor):
        if no != None:
            if no.dado == valor:
                return True
            achou_esq = self.busca_valor(no.esq, valor)
            if achou_esq:
                return True
            achou_dir = self.busca_valor(no.dir, valor)
            return achou_dir
        else:
            return False


if __name__ == '__main__':

    arvore = Arvore_Binaria()

    arvore.root = No(1)
    arvore.root.esq = No(2)
    arvore.root.dir = No(3)

    p = arvore.root.esq
    q = arvore.root.dir

    p.esq = No(-4)
    p.dir = No(5)

    q.esq = No(6)
    q.dir = No(-7)

    print(arvore.nos(arvore.root))
    print(arvore.nos_folhas(arvore.root))
    print(arvore.busca_valor(arvore.root, 7))