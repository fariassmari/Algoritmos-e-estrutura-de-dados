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

class Lista_Encadeada:
    def __init__(self, inicio = None):
        self.__inicio = None

    def eh_vazia(self):
        return self.__inicio is None

    def tamanho(self):
        if self.__inicio is not None:
            contador = 0
            p = self.__inicio
            while p.prox != None:
                contador += 1
                p = p.prox
            return contador

    def adicionar_inicio(self, no):
        if self.__inicio != None:
            no.prox = self.__inicio
            self.__inicio = no
        else:
            self.__inicio = no

    def adicionar_meio(self, posicao, no):
        if posicao >= 1 and posicao < self.tamanho(): 
            if self.__inicio != None:
                p = self.__inicio
                q = None
                i = 1

                while i < posicao:
                    q = p
                    p = p.prox
                    i += 1

                if q is None:
                    no.prox = self.__inicio
                    self.__inicio = no
                else:
                    q.prox = no
                    no.prox = p 
    
    def adicionar_final(self, no):
        if self.__inicio is not None:
            p = self.__inicio
            while p.prox != None:
                p = p.prox
            p.prox = no
        else:
            self.__inicio = no

    def remover_inicio(self):
        if self.__inicio is not None:
            p = self.__inicio
            self.__inicio = p.prox
            p.prox = None
            return p.dado
        return None

    def remover_meio(self, posicao):
        if posicao >= 1 and posicao <= self.tamanho():
            if self.__inicio is not None:
                p = self.__inicio
                q = None
                i = 1 
                while i < posicao:
                    p = p.prox
                    i += 1
                    q = p
                q.prox = p.prox
                return p.dado
    
    def remover_fim(self):
        if self.__inicio is not None:
            p = self.__inicio
            q = None
            while p.prox != None:
                p = p.prox
                q = p
            q.prox = None
            return p.dado
        else:
            return None
        
    def consultar_inicio(self):
        if self.__inicio is not None:
            return self.__inicio
        else:
            return None
    
    def consultar_meio(self, posicao):
        if posicao >= 1 and posicao <= self.tamanho():
            if self.__inicio is not None:
                p = self.__inicio
                i = 1
                while i < posicao:
                    p = p.prox
                    i += 1
                return p.dado
        
    def consultar_fim(self):
        if self.__inicio is not None:
            p = self.__inicio 
            while p.prox != None:
                p = p.prox
            return p.dado
        else:
            return None
        
    def __str__(self):
        saida = 'Lista: ['
        p = self.__inicio

        while p != None:
            saida += f'{p.dado}'
            p = p.prox
            if p != None:
                saida += ', '
        saida += ']'
        return saida
        
if __name__ == '__main__':
    machos = Lista_Encadeada()
    femeas = Lista_Encadeada()

    while True:
        nome_animal = input('Digite o nome do animal: ')
        sexo_animal = input('Digite o sexo do animal: ')

        if sexo_animal == 'macho':
            machos.adicionar_final(No(nome_animal))
        elif sexo_animal == 'femea':
            femeas.adicionar_final(No(nome_animal))
        else:
            print('operação inválida')

        continuar = input('Deseja cadastrar outro animal? (S/N): ')
        if continuar == 'N':
            break

    print(machos)
    print(femeas)

            
