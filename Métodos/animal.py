class Animal:
    raca_registradas = []

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca
        Animal.raca_registradas.append(raca)

    def listar_raca(self):
        for raca in Animal.raca_registradas:
            return raca

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, valor):
        self.__raca = valor
        
a1 = Animal("Rex", "Pastor Alemão")
a2 = Animal("Mimi", "Siames")
a3 = Animal("Bob", "Vira-lata")

a1.raca = "Pincher"
a2.raca = "Salsicha"

print(a1.nome, a1.raca)
print(a1.listar_raca())
print(a2.raca)
        