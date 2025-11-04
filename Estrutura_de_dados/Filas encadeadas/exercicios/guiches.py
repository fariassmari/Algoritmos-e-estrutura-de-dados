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

    @property
    def inicio(self):
        return self.__inicio
    
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

    guiches = Fila_Encadeada()
    clientes = Fila_Encadeada()

    num_guiches = 6
    for i in range(num_guiches + 1):
        guiches.adicionar(No(0))

    prox_senha = 1

    while True:
        opcao = input('1-Adicionar cliente\n2-Atender Cliente\n3-Mostrar fila\n4-Encerrar')

        if opcao == '1':
            clientes.adicionar(No(f'Cliente{prox_senha}'))
            prox_senha += 1

        elif opcao == '2':
            if not clientes.esta_vazia():
                guiche = guiches.inicio
                while guiche != None:
                    if guiche.dado == 0:
                        guiche.dado = clientes.inicio.dado
                        clientes.remover()
                        break
                    guiche = guiche.prox
                    
        elif opcao == '3':
            guiche = guiches.inicio
            numero_guiche = 1
            while guiche is not None:
                if guiche.dado == 0:
                    print(f'Guiche {numero_guiche}: Livre')
                else:
                    print(f'Guiche {numero_guiche}: Atendendo {guiche.dado}')
                guiche = guiche.prox
                numero_guiche += 1
            print(clientes)

        elif opcao == '4':
            break

        else: 
            print('invalido')

