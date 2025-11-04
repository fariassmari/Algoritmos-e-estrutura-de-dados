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

    def parenteses(self):
        if self.__topo != None:
            pilha = Pilha_Encadeada()
            p = self.__topo
            while p != None:
                if p.dado == '(':
                    pilha.empilhar(No('('))
                elif p.dado == ')':
                    if pilha.esta_vazia():
                        return False
                    pilha.desempilhar()
                p = p.prox

            return pilha.esta_vazia()
        
    def binario(self, numero):
        if self.__topo != None:
            binario = Pilha_Encadeada()
            while numero > 0:
                resto = p % 2
                binario.empilhar(No(resto))
                numero = numero // 2

            return binario


    def ordem(self):
        if self.__topo != None:
            p = self.__topo
            while p.prox != None:
                if p.dado > p.prox.dado:
                    p.dado, p.prox.dado = p.prox.dado, p.dado
                p = p.prox

    def espaco(self, no):
        if self.__topo != None:
            if no.dado == ' ':
                return 1 + self.espaco(no.prox)
            else:
                return 0
            

    def qtd_esp(self):
        if p:
            if p[0] == ' ':
                return 1 + self.qtd_esp(p[1:])
        return 0

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

    p.empilhar(No("5"))
    p.empilhar(No("4"))
    p.empilhar(No("78"))
    p.empilhar(No("1"))
    
    parent = Pilha_Encadeada()

    parent.empilhar(No(")"))
    parent.empilhar(No("("))
    parent.empilhar(No(")"))
    parent.empilhar(No("("))

    print(parent.parenteses())

    p.ordem()
    print(p)

    pilha = Pilha_Encadeada()
    numero = int(input("Digite um número inteiro: "))

    pilha.empilhar(No(numero))
    binario = pilha.binario(numero)

    print(f"Representação binária de {numero}: ", end="")
    print(binario)

    

