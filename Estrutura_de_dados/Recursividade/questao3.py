from Estrutura_de_dados.Listas_encadeadas.listas import Lista_Encadeada, No

def soma(lista, no=None):
    if no is None:
        no = lista.inicio
    if no is None:
        return 0
    return no.dado + soma(lista, no.prox)
    
if __name__ == '__main__':
    lista = Lista_Encadeada()

    lista.adicionar_final(No(7))
    lista.adicionar_final(No(1))
    lista.adicionar_final(No(2))

    print(lista)           # Lista: [7, 1, 2]
    print(soma(lista))     # 10
