class Exame_Linear:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def _hash_(self, chave, i):
        return ((chave % self.tamanho) + i) % self.tamanho

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
            index = self._hash_(chave,i)
            if self.tabela[index] is None:
                return None
            elif self.tabela[index][0] == chave:
                return self.tabela[index][1]
            i += 1
        return None

if __name__ == "__main__":
    ht = Exame_Linear(11) # Tamanho da tabela

    ht.inserir(10, "Maçã")
    ht.inserir(22, "Banana")
    ht.inserir(34, "Laranja")
    ht.inserir(1, "Uva")
    ht.inserir(12, "Abacaxi")
    ht.inserir(63, "Pera")

    print("\nTabela Hash:")
    print(ht)

    print("\nBuscando 22:", ht.buscar(22))
    print("Buscando 10:", ht.buscar(10))
    print("Buscando 63:", ht.buscar(63))
    print("Buscando 99 (inexistente):", ht.buscar(99))