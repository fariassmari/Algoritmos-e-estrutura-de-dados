class Escola:
    def __init__(self):
        self.__alunos = []
        self.__professores = []

    def adicionar_aluno(self, aluno):
        self.__alunos.append(aluno)
    
    def adicionar_professores(self, professor):
        self.__professores.append(professor)

    def remover_aluno(self, procurar_aluno):
        for i, aluno in enumerate(self.__alunos):
            if aluno.nome == procurar_aluno:
                return self.__alunos.pop(i)
        return None
    
    def remover_professor(self, procurar_professor):
        for i, professor in enumerate(self.__professores):
            if professor.nome == procurar_professor:
                return self.__professores.pop(i)
        return None
    
    def __str__(self):
        resultado = '=== Escola ===\n'

        resultado += '\n-- Alunos --\n'
        if self.__alunos:
            for aluno in self.__alunos:
                resultado += str(aluno) + '\n'
        else:
            resultado += 'Nenhum aluno cadastrado. \n'

        resultado += '\n-- Professores --\n'
        if self.__professores:
            for professor in self.__professores:
                resultado += str(professor) + '\n'
        else:
            resultado += 'Nenhum professor cadastrado.\n'
        
        return resultado


class Aluno:
    def __init__(self, nome, idade, matricula):
        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula 

    # Método get
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def matricula(self):
        return self.__matricula
    
    # Método set
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    @idade.setter
    def idade(self, valor):
        self.__idade = valor
    @matricula.setter
    def matricula(self, valor):
        self.__matricula = valor

    def __str__(self):
        return f'Aluno: {self.__nome}, Idade: {self.__idade}, Matrícula: {self.__matricula}'

class Professor:
    def __init__(self, nome, idade, matricula, especialidade):
        self.__nome = nome
        self.__idade = idade 
        self.__matricula = matricula
        self.__especialidade = especialidade


    # Método get
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def matricula(self):
        return self.__matricula
    @property
    def especialidade(self):
        return self.__especialidade
    
    # Método set
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    @idade.setter
    def idade(self, valor):
        self.__idade = valor
    @matricula.setter
    def matricula(self, valor):
        self.__matricula = valor
    @especialidade.setter
    def especialidade(self, valor):
        self.__especialidade = valor

    def __str__(self):
        return f'Professor: {self.__nome}, Idade: {self.__idade}, Matrícula: {self.__matricula}, Especialidade: {self.__especialidade}'

### MAIN
if __name__ == '__main__':
    aluno1 = Aluno("João", 20, "2023001")
    aluno2 = Aluno("Ana", 19, "2023002")
    aluno3 = Aluno("Pedro", 21, "2023003")
    aluno4 = Aluno("Maria", 22, "2023004")

    professor1 = Professor("Carlos", 40, "P101", "Matemática")
    professor2 = Professor("Luciana", 35, "P102", "História")
    professor3 = Professor("Roberto", 50, "P103", "Física")
    professor4 = Professor("Fernanda", 30, "P104", "Biologia")

    escola1 = Escola()

    for aluno in [aluno1, aluno2, aluno3, aluno4]:
        escola1.adicionar_aluno(aluno)

    for professor in [professor1, professor2, professor3, professor4]:
        escola1.adicionar_professores(professor)

    print(escola1)


    
