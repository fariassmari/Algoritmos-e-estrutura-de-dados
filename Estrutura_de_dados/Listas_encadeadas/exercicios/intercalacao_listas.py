from questao1 import No, Lista_Encadeada
import random

if __name__ == '__main__':
    l1 = Lista_Encadeada()
    l2 = Lista_Encadeada()
    l3 = Lista_Encadeada()

    for i in range(6):
        num = random.randint(1, 150)
        l1.adicionar_final(No(num))

    for i in range(6):
        num = random.randint(1, 150)
        l2.adicionar_final(No(num))

    print(l1)
    print(l2)

    l1.ordenar()
    l2.ordenar()

    p = l1.inicio
    while p != None:
        l3.adicionar_final(No(p.dado))
        p = p.prox

    q = l2.inicio
    while q != None:
        l3.adicionar_final(No(q.dado))
        q = q.prox

    print(l3)

    l3.ordenar()
    print(l3)
        
    print(l1)
    print(l2)

