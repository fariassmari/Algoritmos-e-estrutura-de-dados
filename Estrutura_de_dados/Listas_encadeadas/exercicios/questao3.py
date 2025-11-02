from questao1 import No, Lista_Encadeada
import random

if __name__  == '__main__':
    # a) crie quatro listas (L1, L2, L3 e L4);
    L1 = Lista_Encadeada()
    L2 = Lista_Encadeada()
    L3 = Lista_Encadeada()
    L4 = Lista_Encadeada()

    # b) insira sequencialmente, na lista L1, 10 números inteiros obtidos de forma randômica (entre 0 e 99);
    for i in range(10):
        num = random.randint(0, 99)
        L1.adicionar_final(No(num))
    print(L1)

    # c) idem para a lista L2;
    for i in range(10):
        num = random.randint(0,99)
        L2.adicionar_final(No(num))
    print(L2)
    
    # d) concatene as listas L1 e L2, armazenando o resultado na lista L3;
    """p = L1.inicio 
    while p.prox != None:
        p = p.prox
    p.prox = L2.inicio
    L3 = L1
    print(L3)"""

    p = L1.inicio
    while p != None:
        L3.adicionar_final(No(p.dado))
        p = p.prox

    q = L2.inicio
    while q != None:
        L3.adicionar_final(No(q.dado))
        q = q.prox

    print(L3)

    # e) armazene na lista L4 os elementos da lista L3 (na ordem inversa);
    r = L3.inicio
    while r != None:
        L4.adicionar_inicio(No(r.dado))
        r = r.prox
    print(L4)

    def inversa(lista):
        def no_inverso(no):
            if no == None:
                return 0
            else:
                return no_inverso(no.prox)
        return no_inverso(lista.inicio)
    




