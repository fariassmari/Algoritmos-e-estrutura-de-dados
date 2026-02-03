class Hashing_Duplo:
    def __init__(self, tamanho, mLinha):
        self.tamanho = tamanho
        self.mLinha = mLinha
        self.tabela = [None] * tamanho

    def _hash_(self, chave, i):
        return (self._hash1(chave) + i * self._hash2(chave)) % self.tamanho
    
    def _hash1(self, chave):
        return chave % self.tamanho

    def _hash2(self, chave):
        return 1 + (chave % self.mLinha)

    def inserir(self, chave, valor):
        index = self._hash_(chave,0)

        if self.tabela[index] is None:
            self.tabela[index] = (chave, valor)
        else:
            i = 1
            while i < self.tamanho:
                new_index = self._hash_(chave, i)

                if self.tabela[new_index] is None:
                    self.tabela[new_index] = (chave, valor)
                    break
                else:
                    i += 1
            else:
                print("Tabela cheia.")

    def __str__(self):
        return str(self.tabela)
    
    def buscar(self, chave):
        i = 0 
        while i < self.tamanho:
            index = self._hash_(chave, i)
            if self.tabela[index] is None:
                return None
            elif self.tabela[index][0] == chave:
                return self.tabela[index][1]
            i += 1
        return None
    
if __name__ == "__main__":
    ht = Hashing_Duplo(11,9) # Tamanho da tabela

    ht.inserir(37, "Maçã")
    ht.inserir(83, "Banana")
    ht.inserir(97, "Laranja")
    ht.inserir(78, "Uva")
    ht.inserir(14, "Abacaxi")
    ht.inserir(59, "Pera")
    ht.inserir(25, "Morango")
    ht.inserir(72, "Ameixa")

    print("\nTabela Hash:")
    print(ht)