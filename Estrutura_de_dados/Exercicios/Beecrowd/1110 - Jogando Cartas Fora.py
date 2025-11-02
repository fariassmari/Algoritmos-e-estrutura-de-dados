class Fila:
    def __init__(self, itens=[]):
        if itens is None:
            self.__itens = []
        else:
            self.__itens = itens

    def adicionar(self, item):
        self.__itens.append(item)

    def remover(self):
        if not self.eh_vazia():
            return self.__itens.pop(0)
    
    def eh_vazia(self):
        return self.__itens == []
    
    def tamanho(self):
        return len(self.__itens)

class Cartas:
    def __init__(self, numero):
        self.__numero = numero

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    def jogar(self):
        jogo1 = Fila()

        for i in range(1, self.__numero + 1):
            jogo1.adicionar(i)
        cartas_removidas = []
        
        while jogo1.tamanho() > 1:
            cartas_removidas.append(jogo1.remover())
            jogo1.adicionar(jogo1.remover())
        carta_final = jogo1.remover()
        return cartas_removidas, carta_final
    
### MAIN
if __name__ == '__main__':
    try:
        while True:
            numero = int(input())
            if numero == 0:
                break
            cartas = Cartas(numero)
            removidas, final = cartas.jogar()
            
            print("Discarded cards:", end=" ")
            if removidas:
                print(", ".join(map(str, removidas)))
            else:
                print()
            print(f"Remaining card: {final}")
    except EOFError:
        pass