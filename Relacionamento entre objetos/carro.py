# Classe Carro
class Carro:
    # Método Construtor (Inicialização)
    def __init__(self, cor, placa, motor, dimensao):
        self. __cor = cor
        self.__placa = placa
        self.__motor = motor
        self.__dimensao = dimensao

    # Métodos acessadores
    @property
    def cor(self):
        return self.__cor
    @property
    def placa(self):
        return self.__placa
    @property
    def motor(self):
        return self.__motor
    @property
    def dimensao(self):
        return self.__dimensao
    
    # Métodos alteradores
    @cor.setter
    def cor(self, valor):
        self.__cor = valor
    @placa.setter
    def placa(self, valor):
        self.__placa = valor
    @motor.setter
    def motor(self, valor):
        self.__motor = valor
    @dimensao.setter
    def dimensao(self, valor):
        self.__dimensao = valor

    # Método string
    def __str__(self):
        return f'Cor: {self.__cor}, Placa: {self.__placa}, \nMotorização: {self.__motor}, \nDimensão: {self.__dimensao}'
    
# Classe Motor
class Motor:
    # Método construtor
    def __init__(self, motorizacao, combustivel='flex'):
        self.__motorizacao = motorizacao
        self.__combustivel = combustivel

    # Métodos acessadores
    @property
    def motorizacao(self):
        return self.__motorizacao
    @property
    def combustivel(self):
        return self.__combustivel
    
    # Métodos alterados
    @motorizacao.setter
    def motorizacao(self, valor):
        self.__motorizacao = valor
    @combustivel.setter
    def combustivel(self, valor):
        self.__combustivel = valor

    # Método string
    def __str__(self):
        return f'Motor: {self.__motorizacao}L, Combustivel: {self.__combustivel}'
        
# Classe Dimensão
class Dimensao:
    # Método construtor
    def __init__(self, altura, largura, comprimento):
        self.__altura = altura
        self.__largura = largura
        self.__comprimento = comprimento

    # Métodos acessadores
    @property
    def altura(self):
        return self.__altura
    @property 
    def largura(self):
        return self.__largura
    @property
    def comprimento(self):
        return self.__comprimento
    
    # Métodos alteradores
    @altura.setter
    def altura(self, valor):
        self.__altura = valor
    @largura.setter
    def largura(self, valor):
        self.__largura = valor
    @comprimento.setter
    def comprimento(self, valor):
        self.__comprimento = valor

    def __str__(self):
        return f'Altura: {self.__altura}, Largura: {self.__largura}, Comprimento: {self.__comprimento}'
    

### MAIN

if __name__ == '__main__':
    motor = Motor('1.6', 'Gasolina')
    dimensao = Dimensao(1.67, 1.81, 4.37)
    carro = Carro('preto', 'XXX1234', motor, dimensao)

    print(carro)