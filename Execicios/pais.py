class Pais:
    def __init__(self, nome, capital, dimensao):
        self.__nome = nome
        self.__capital = capital
        self.__dimensao = dimensao
        self.__paises_fronteira = []

    @property
    def nome(self):
        return self.__nome
    @property
    def capital(self):
        return self.__capital
    @property
    def dimensao(self):
        return self.__dimensao

    def retorna(self):
        return self.__paises_fronteira

    def adicionar_fronteira(self, pais_fronteira):
        if pais_fronteira not in self.__paises_fronteira and pais_fronteira != self:
            self.__paises_fronteira.append(pais_fronteira)

    def __str__(self):
        return f'Nome: {self.__nome}, Capital: {self.__capital}, Dimensão: {self.__dimensao}'

if __name__ == '__main__':
    brasil = Pais("Brasil", "Brasília", 8_515_767)
    argentina = Pais("Argentina", "Buenos Aires", 2_780_400)
    uruguai = Pais("Uruguai", "Montevidéu", 176_215)

    # Adicionando fronteiras
    brasil.adicionar_fronteira(argentina)
    brasil.adicionar_fronteira(uruguai)

    argentina.adicionar_fronteira(brasil)
    uruguai.adicionar_fronteira(brasil)

    # Mostrando informações
    print(brasil)
    print("Fronteiras do Brasil:")
    for pais in brasil.retorna():
        print(f" - {pais.nome}")

    print("\n", argentina)
    print("Fronteiras da Argentina:")
    for pais in argentina.retorna():
        print(f" - {pais.nome}")


