class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    @property
    def mes(self):
        return self.__mes
    @property
    def ano(self):
        return self.__ano
    
    @dia.setter
    def dia(self, valor):
        self.__dia = valor
    @mes.setter
    def mes(self, valor):
        self.__mes = valor
    @ano.setter
    def ano(self, valor):
        self.__ano = valor

    def __str__(self):
        return f'Data: {self.__dia}/{self.__mes}/{self.__ano}'
    
if __name__ == '__main__':
    data1 = Data(16, 12, 2025)
    data2 = Data(6, 9, 2022)

    print(data1)
    print(data2)

