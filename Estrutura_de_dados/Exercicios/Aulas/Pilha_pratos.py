class Pilha:
    def __init__(self, itens = []):
        self.__itens = itens

    def empilhar(self, item):
        return self.__itens.append(item)
    
    def desempilhar(self, item):
        return self.__itens.pop(item)
    
    def eh_vazio(self):
        return self.__itens == []
    
    def topo(self):
        return self.__itens[len(self.__itens)-1]
    
    def tamanho(self):
        return len(self.__itens)
    
    def __str__(self):
        return f'{self.__itens}'
    
### MAIN
if __name__ == '__main__':
    pratos = Pilha()

    for i in range(10):
        pratos.empilhar(i)

    print(pratos)
    print(pratos.topo())
    print(pratos.desempilhar(1))
    print(pratos)
