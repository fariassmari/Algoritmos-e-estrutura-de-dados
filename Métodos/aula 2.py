class Conta_Bancaria:
    def __init__(self, nome, cpf, conta, saldo):
        self.nome = nome
        self.cpf = cpf
        self.conta = conta
        self.saldo = saldo

    def debitar(self, saldo, valor):
        if self.saldo >= valor:
            return self.saldo - valor
        else:
            return "Saldo insuficiente"

    def creditar(self, saldo, valor):
        self.saldo += valor
        return self.saldo
    
conta1 = Conta_Bancaria('Maria', 10000000, 123, 1000)

print(conta1.creditar(1000, 400))

print(conta1.debitar(1000, 200))

