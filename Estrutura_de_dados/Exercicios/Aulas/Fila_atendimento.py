class Fila:
    def __init__(self, itens = []):
        self.__itens = itens

    def eh_vazia(self):
        return self.__itens == []

    def adicionar(self, item):
        self.__itens.append(item)

    def remover(self):
        return self.__itens.pop(0)
    
    def tamanho(self):
        return len(self.__itens)

    def topo(self):
        return self.__itens[len(self.__itens)-1]
    
    def __str__(self):
        return f'{self.__itens}'

### MAIN

if __name__ == '__main__':
    atendimento = Fila()

    for i in range(10):
        atendimento.adicionar(i)

    print(atendimento)
    print(atendimento.topo())

    print(atendimento.remover())

    