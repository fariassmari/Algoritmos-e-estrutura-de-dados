class Aluno:
    def __init__(self, matricula, nome):
        self.__matricula = matricula
        self.__nome = nome
        self.__notas = []

    @property
    def matricula(self):
        ano = str(self.__matricula)[:4]
        periodo = str(self.__matricula)[4]
        codigo = str(self.__matricula)[5:]
        return f'{ano}.{periodo}.{codigo}'
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    def adicionar_nota(self, nota):
        self.__notas.append(nota)

    def media(self):
        soma = 0
        for nota in self.__notas:
            soma += nota
        media = soma / len(self.__notas)
        return media


    def __str__(self):
        return f'Nome: {self.__nome}\nMatrícula: {self.matricula}\nMédia: {self.media():.2f}'
    

if __name__ == '__main__':
    aluno1 = Aluno("2025145", "Mariana")
    aluno1.adicionar_nota(8)
    aluno1.adicionar_nota(7)
    aluno1.adicionar_nota(9)

    print(aluno1)
