from questao1 import No, Lista_Encadeada
import random

if __name__ == "__main__":
    par = Lista_Encadeada()
    impar = Lista_Encadeada()
    
    for i in range(20):
        num = random.randint(1, 120)
        if num % 2 == 0:
            par.adicionar_final(No(num))
        else:
            impar.adicionar_final(No(num))

    print(par)
    print(impar)