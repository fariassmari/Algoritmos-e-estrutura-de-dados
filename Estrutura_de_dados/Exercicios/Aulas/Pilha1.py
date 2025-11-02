class Pilha:
    def __init__(self, itens=[]):
        self.__itens = []

    def eh_vazia(self):
        return self.__itens == []
    
    def empilhar(self, item):
        self.__itens.insert(0, item)

    def desempilhar(self, item):
        return self.__itens.pop(0)

    def topo(self):
        return self.__itens[0]
    
    def tamanho(self):
        return len(self.__itens)

    def __str__(self):
        return f'{self.__itens}'
    
if __name__ == '__main__':
    pilha1 = Pilha()

    for i in range(8):
        pilha1.empilhar(i + 1)

    print(pilha1)
    print(pilha1.topo())
    print(pilha1.tamanho())
    print(pilha1.desempilhar(3))

        
    
