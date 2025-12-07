class Indice_Chave:
    def __init__(self):
        self.__chave = 0
        self.__indice = 0

    @property
    def chave(self):
        return self.__chave
    @chave.setter
    def chave(self, nova_chave):
        self.__chave = nova_chave

    @property
    def indice(self):
        return self.__indice
    @indice.setter
    def indice(self, novo_indice):
        self.__indice = novo_indice

class No:
    ordem = 4

    def __init__(self, chaves):
        self.__chaves = [None] * (No.ordem - 1)
        self.__filhos = [None] * No.ordem
        self.__nFilhos = len(chaves) + 1

        for i in range(len(chaves)):
            item = Indice_Chave()
            item.indice = i
            item.chave = chaves[i]
            self.__chaves = item

    @property
    def chaves(self):
        return self._chaves

    @property
    def filhos(self):
        return self._filhos

    @property
    def nFilhos(self):
        return self._nFilhos

    @chaves.setter
    def chaves(self, chaves):
        self._chaves = chaves

    @filhos.setter
    def filhos(self, filhos):
        self._filhos = filhos

    @nFilhos.setter
    def nFilhos(self, nFilhos):
        self._nFilhos = nFilhos

class Arvore_Multi:
    def __init__(self):
        self.__raiz = None

    @property
    def raiz(self):
        return self.__raiz

    @raiz.setter
    def raiz(self, raiz):
        self.__raiz = raiz

    def busca_em_no(self, chave, no):
        n_Chaves = no.nFilhos - 1
        for i in range(n_Chaves):
            if chave <= no.chaves[i].chave:
                return i
        return n_Chaves
    
    def busca_multi(self, chave, no):
        arvore = self.__raiz

        while arvore != None:
            i = self.busca_em_no(chave, arvore)
            if i < arvore.nFilhos - 1:
                itemChave = arvore.chaves[i].chave
                if chave == itemChave:
                    return  arvore.chaves[i].indice
                
            arvore = arvore.filhos[i]

        return -1
     
    def caminhamento(self, no):
        if no != None:
            for i in range(no.nFilhos - 1):
                self.caminhamento(no.filhos[i])
                print(no.chaves[i].chave)
            self.caminhamento(no.filhos[no.nFilhos - 1])

    def set_filho(self, pai, posicao, no):
        pai.filhos[posicao] = no

