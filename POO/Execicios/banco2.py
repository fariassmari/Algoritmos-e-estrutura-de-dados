class Conta_Corrente:
    def __init__(self, numero, saldo, nome_titular):
        self.__numero = numero
        self.__saldo = saldo
        self.__nome_titular = nome_titular

    @property
    def numero(self):
        return self.__numero
    @property
    def saldo(self):
        return self.__saldo
    @property
    def nome_titular(self):
        return self.__nome_titular
    
    @numero.setter
    def numero(self, valor):
        self.__numero = valor
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor
    @nome_titular.setter
    def nome_titular(self, valor):
        self.__nome_titular = valor      

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False

    def sacar(self, valor):
        if valor > 0 and self.__saldo >= valor:
            self.__saldo -= valor
            return True
        return False
        
    def __str__(self):
        return f'Conta: {self.__numero}, Titular: {self.__nome_titular}, Saldo: R${self.__saldo}'

class Banco:
    def __init__(self):
        self.__banco = []

    def adicionar_conta(self, nova_conta):
        self.__banco.append(nova_conta)

    def remover_conta(self, numero_conta):
        for conta in self.__banco:
            if conta.numero == numero_conta :
                self.__banco.remove(conta)
                return conta
            
    def buscar_conta(self, numero):
        for conta in self.__banco:
            if conta.numero == numero:
                return conta
        return None
    
    def transferir(self, numero_origem, numero_destino, valor):
        conta_origem = self.buscar_conta(numero_origem)
        conta_destino = self.buscar_conta(numero_destino)
        if conta_origem and conta_destino:
            if conta_origem.sacar(valor):
                conta_destino.depositar(valor)
            else:
                return 'Saldo insuficiente'

    def depositar(self, numero, valor):
        conta = self.buscar_conta(numero)
        if conta:
            return conta.depositar(valor)
        return False

    def sacar(self, numero, valor):
        conta = self.buscar_conta(numero)
        if conta:
            return conta.sacar(valor)
        return False

    def somar_saldos(self):
        total = 0
        for conta in self.__banco:
            total += conta.saldo
        return total


### MAIN
    
if __name__ == '__main__':
    banco = Banco()

    c1 = Conta_Corrente("001", 1000, "Ana")
    c2 = Conta_Corrente("002", 500, "João")
    c3 = Conta_Corrente("003", 200, "Maria")

    banco.adicionar_conta(c1)
    banco.adicionar_conta(c2)
    banco.adicionar_conta(c3)

    print("Saldo total do banco:", banco.somar_saldos())

    banco.depositar("002", 300)
    print(c2)

    banco.sacar("001", 200)
    print(c1)

    banco.transferir("002", "003", 100)
    print(c2)
    print(c3)

    print("Saldo total do banco:", banco.somar_saldos())





