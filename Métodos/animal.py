class Animal:
    raca_registradas = []

    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca
        Animal.raca_registradas.append(raca)

    def listar_raca(self):
        for raca in Animal.raca_registradas:
            return raca
        
a1 = Animal("Rex", "Pastor Alemão")
a2 = Animal("Mimi", "Siames")
a3 = Animal("Bob", "Vira-lata")

print(a1.nome, a1.raca)
print(a1.listar_raca())
        