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
        # a) Cria a lista vazia
        self.__inicio = None

    @property
    def inicio(self):
        return self.__inicio

    # b) Verifica se a lista é vazia
    def eh_vazia(self):
        return self.__inicio is None

    # c) Verifica o tamanho da lista
    def tamanho(self):
        if self.__inicio is not None:
            contador = 0
            p = self.__inicio
            while p.prox != None:
                contador += 1
                p = p.prox
            return contador
        
    # d) Obtem o valor do elemento pela posição dada 
    def valor_elemento(self, posicao):
        if self.__inicio is not None and posicao > 0:
            p = self.__inicio
            contador = 0 
            while p != None:
                if contador == posicao:
                    return p.dado
                p = p.prox
                contador += 1
            return p.dado
        else:
            return None
    
    # e) Obtem a posição do elemento pelo valor dado
    def posicao_elemento(self, valor):
        if self.__inicio is not None:
            p = self.__inicio
            contador = 0 
            while p is not None:
                if p.dado == valor:
                    return contador
                contador += 1
                p = p.prox
            return contador
        else:
            return None

    # f) Inserir um dado elemento na primeira posição;
    def adicionar_inicio(self, no):
        if self.__inicio != None:
            no.prox = self.__inicio
            self.__inicio = no
        else:
            self.__inicio = no

    # g) Inserir um dado elemento na última posição;
    def adicionar_final(self, no):
        if self.__inicio is not None:
            p = self.__inicio
            while p.prox != None:
                p = p.prox
            p.prox = no
        else:
            self.__inicio = no

    # h) Inserir um dado elemento em uma posição dada;
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
    
    # i) Remover o primeiro elemento;
    def remover_inicio(self):
        if self.__inicio is not None:
            p = self.__inicio
            self.__inicio = p.prox
            p.prox = None
            return p.dado
        return None

    # j) Remover o último elemento;
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
    
    
    def remover_pelo_valor(self, valor):
        if self.__inicio is not None:
            p = self.__inicio
            if p.dado == valor:
                removido = p.dado
                self.__inicio = p.prox
                return removido
            else:
                while p.prox != None:
                    if p.prox.dado == valor:
                        removido = p.prox.dado
                        p.prox = p.prox.prox
                        return removido
                    p = p.prox         
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
        
    def esvazia_lista(self):
        return self.__inicio == None
    
    def ordenar(self):
        if self.__inicio != None:
            p = self.__inicio
            while p != None:
                no_menor = p
                q = p.prox
                while q != None:
                    if q.dado < no_menor.dado:
                        no_menor = q
                    q = q.prox
                
                if no_menor != p:
                    troca = p.dado
                    p.dado = no_menor.dado
                    no_menor.dado = troca
                
                p = p.prox

    def contar(self, valor):
        if self.__inicio != None:
            p = self.__inicio
            ocorrencias = 0
            while p != None:
                if p.dado == valor:
                    ocorrencias += 1
                p = p.prox

            return ocorrencias         
        
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
    lista = Lista_Encadeada()

    lista.adicionar_final(No(1))
    lista.adicionar_final(No(1))
    lista.adicionar_final(No(2))
    lista.adicionar_final(No(2))
    lista.adicionar_final(No(3))

    print(lista.valor_elemento(2))