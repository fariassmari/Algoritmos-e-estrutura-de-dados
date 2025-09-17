class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula 

class Professor:
    def __init__(self, nome, idade, matricula, especialidade):
        self.nome = nome
        self.idade = idade 
        self.matricula = matricula
        self.especialidade = especialidade


aluno1 = Aluno("João", 20, "2023001")
professor1 = Professor("Maria", 35, "P123", "Matemática")

print(f"Aluno: {aluno1.nome}, Idade: {aluno1.idade}, Matrícula: {aluno1.matricula}")
print(f"Professor: {professor1.nome}, Idade: {professor1.idade}, Matrícula: {professor1.matricula}, Especialidade: {professor1.especialidade}")
    
