from pilhas import No, Pilha_Encadeada
from filas import Fila_Encadeada

if __name__ == '__main__':

    p = Fila_Encadeada()

    p.adicionar(No("A"))
    p.adicionar(No("B"))
    p.adicionar(No("C"))
    p.adicionar(No("D"))

    pilha = Pilha_Encadeada()

    def inverter(fila):
        if fila.inicio != None:
            p = fila.inicio 
            while p != None:
                pilha.empilhar(No(p.dado))
                p = p.prox

            return pilha
        
    resultado = inverter(p)
    print(resultado)