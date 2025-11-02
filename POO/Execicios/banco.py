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

    def sacar(self, valor):
        if self.__saldo > 0 and self.__saldo >= valor:
            self.__saldo -= valor
            return True
        else:
            return False
        
    
        
    def __str__(self):
        return f'Conta: {self.__numero}, Titular: {self.__nome_titular}, Saldo: R${self.__saldo}'

### MAIN
banco = []

for i in range(5):
    numero, saldo, nome_titular = input('Digite o número, saldo e nome do titular da conta: (número,saldo,nome_titula)').split(',')

    saldo = float(saldo)

    conta = Conta_Corrente(numero, saldo, nome_titular)
    banco.append(conta)

def buscar_conta(numero):
    for conta in banco:
        if conta.numero == numero:
            return conta
    return None

while True:
    menu = input('Digite a operação(1-Depositar, 2-Sacar, 3-Saldo e 4-Sair):')

    if menu == '1':
        num, valor = input('Digite o numero da conta e o valor a ser depositado: (numero,valor) ').split(',')
        valor = float(valor)
        conta = buscar_conta(num)

        if conta:
            conta.depositar(valor)
            print('Deposito realizado com sucesso')
        else:
            print('Conta não encontrada')


    elif menu == '2':
        num, valor = input('Digite o numero da conta e o valor a ser sacado: (numero,valor) ').split(',')
        valor = float(valor)
        conta = buscar_conta(num)

        if conta:
            if conta.sacar(valor):
                print('Saque realizado com sucesso')
            else:
                print('Saldo insuficiente ou valor inválido')
        else:
            print('Conta não encontrada')

    elif menu == '3':
        num = input('Digite o numero da conta: (numero) ')
        conta = buscar_conta(num)

        if conta:
            print(conta)
        else:
            print('Conta não encontrada')

    elif menu == '4':
        break

    else:
        print('Operação inválida.')





