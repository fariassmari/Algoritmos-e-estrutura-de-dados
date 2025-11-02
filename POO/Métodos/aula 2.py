class Conta_Corrente:
    def __init__(self, nome, cpf, conta, saldo = 0):
        self.__nome = nome
        self.__cpf = cpf
        self.__conta = conta
        self.__saldo = saldo

    def debitar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return self.__saldo
        else:
            return "Saldo insuficiente"

    def creditar(self, valor):
        self.__saldo += valor
        return self.__saldo
    
    def transferir(self, valor, destino):
        if self.__saldo >= valor:
            self.__saldo -= valor
            destino.saldo += valor
        else:
            return "Saldo insuficiente"
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, valor):
        self.__cpf = valor

    @property # Método Get - Retorna o valor do atributo acessado
    def conta(self):
        return self.__conta

    @conta.setter # Método Set - Altera o valor dos atributos
    def conta(self, valor):
        self.__conta = valor
    
    @property # Método Get - Retorna o valor do atributo acessado
    def saldo(self):
        return self.__saldo
    
    @saldo.setter # Método Set - Altera o valor dos atributos
    def saldo(self, valor):
        self.__saldo = valor

# Classe Banco
class Banco:
    def __init__(self):
        self.__contas = []

    def adicionar_contas(self, conta):
        self.__contas.append(conta)

    def somar_saldo(self):
        soma = 0
        for conta in self.__contas:
            soma += conta.saldo
        return soma

    def remover_conta(self, numero):
        for i, conta in enumerate(self.__contas):
            if conta.conta == numero:
                return self.__contas.pop(i)
        return None
    
class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
    @property
    def cpf(self):
        return self.__cpf
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    @cpf.setter
    def cpf(self, valor):
        if len(valor) == 11:
            self.__cpf = valor

    def __str__(self):
        return f"Cliente: Nome: {self.__nome} e CPF: {self.__cpf}"
    

### MAIN
    
if __name__ == "__main__":
  # Criando clientes
  cliente1 = Cliente('Mariana', 12345678910)
  cliente2 = Cliente('Marina', 12345678910)
  cliente3 = Cliente('Maria', 12345678910)

  # Criando contas
  conta1 = Conta_Corrente(cliente1.nome, cliente1.cpf, 1234, 1000)
  conta2 = Conta_Corrente(cliente2.nome, cliente2.cpf, 1230, 800)
  conta3 = Conta_Corrente(cliente3.nome, cliente3.cpf, 1200, 1200)

  # Usando o método transferencia
  conta1.transferir(250, conta2)

  # Criando banco e adicionando contas
  banco1 = Banco()
  banco1.adicionar_contas(conta1)
  banco1.adicionar_contas(conta2)
  banco1.adicionar_contas(conta3)

  print("Saldo total no banco: ", banco1.somar_saldo())

  removida = banco1.remover_conta(1200)
  if removida:
    print(f"Conta {removida.conta} removida com sucesso!")
  else:
    print("Conta não encontrada")

  print("Saldo total após remoção:", banco1.somar_saldo())
  print(cliente1)

