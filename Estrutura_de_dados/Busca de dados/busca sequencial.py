import random

class Registro:
    def __init__(self):
        self.__registros = [] 
    
    @property
    def registros(self):
        return self.__registros
    @registros.setter
    def registros(self, novo_registros):
        self.__registros = novo_registros

    def recebe_registros(self, registro):
        self.registros.append(registro)

    def encontra_indice(self, chave, chaves):
        for i in range(len(chaves)):
            if chaves[i] == chave:
                return i # Retorna o indice que está a chave procurada
        return -1
    
    def busca_insere2(self, chave, chaves, tabela):
        p = tabela
        q = None
        i = 0
        while p != None:
            if chaves[i] == chave:
                return tabela, p.registro
            q = p
            p = p.prox
            i += 1

        
        chaves.append(chave)
        r = No()
        self.recebe_registros(r) 
        r.prox = None

        if tabela == None:
            tabela = r
        else: 
            q.prox = r

        return tabela, r.registro
    
    def __str__(self):
        return f"[Registro: Nome={self._nome}]"

class No:
    def __init__(self):
        self.__registro = None  
        self.__prox = None   
        
    @property
    def registro(self):
        return self.__registro
    @registro.setter
    def registro(self, novo_registro):
        self.__registro = novo_registro

    @property
    def prox(self):
        return self.__prox
    @prox.setter
    def prox(self, novo_prox):
        self.__prox = novo_prox

def encontra_indice_insere(chave, chaves, registros):
        for i in range(len(chaves)):
            if chaves[i] == chave:
                return i
        
        chaves.append(chave)
        return len(registros) 

registro = Registro()
tabela = None
chaves = []

for i in range(10):
    num = random.randint(1, 20)
    chaves.append(num)



print(chaves)

tabela, resultado = registro.busca_insere2(12, chaves, tabela)
print("Chaves depois:", chaves)
print("Resultado do método:", resultado)
