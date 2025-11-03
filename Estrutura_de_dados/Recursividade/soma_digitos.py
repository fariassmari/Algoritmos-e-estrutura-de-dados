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

    @property
    def inicio(self):
        return self.__inicio

    def eh_vazia(self):
        return self.__inicio is None

    def tamanho(self):
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

    def soma(self):
        def _soma(no):
            if no is None:
                return 0
            else: 
                return no.dado + _soma(no.prox)
        return _soma(self.__inicio)

    def inversao(self):
        def _inversao(no):
            if no is None or no.prox is None:
                return no
            
            novo_inicio = _inversao(no.prox)

            no.prox.prox = no
            no.prox = None

            return novo_inicio

        self.__inicio = _inversao(self.__inicio)
            
    def cont(self):
        def _cont(no):
            if no == None:
                return 0
            else:
                return 1 + _cont(no.prox)
        return _cont(self.__inicio)
        
        
if __name__ == '__main__':
    lista = Lista_Encadeada()

    # adicionar
    no = input('Digite a palavra: ')
    for c in no:
        lista.adicionar_final(No(c))
    
    print(lista.cont())
    lista.inversao()
    print(lista)
    


            


