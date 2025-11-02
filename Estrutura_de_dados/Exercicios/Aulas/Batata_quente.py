from Fila import Fila

def batata_quente(criancas, num):
    fila1 = Fila()
    for nome in criancas:
        fila1.adicionar(nome)

    while fila1.tamanho() > 1:
        for i in range(num):
            fila1.adicionar(fila1.remover())
        eliminado = fila1.remover()
    
    return eliminado

lista = ["Carlos", "Joao", "Maria", "Julia", "Tadeu", "Lara"]
print(batata_quente(lista, 3))