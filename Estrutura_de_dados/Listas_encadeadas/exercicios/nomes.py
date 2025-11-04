from questao1 import No, Lista_Encadeada

def comeca_a(palavra):
    for c in palavra:
        if c == 'a' or c == 'A':
            return True
        else:
            return False
    return False

if __name__ == "__main__":
    nomes = Lista_Encadeada()
    
    while True:
        nome = input('Digite o nome de uma pessoa: ')

        if nome == 'break':
            break        
                
        nomes.adicionar_final(No(nome))

    p = nomes.inicio
    while p != None:
        if comeca_a(p.dado):
            nomes.remover_pelo_valor(p.dado)
        p = p.prox

    print(nomes)

