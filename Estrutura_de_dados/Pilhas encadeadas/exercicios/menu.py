from pilhas import No, Pilha_Encadeada

if __name__ == '__main__':
    pilha = Pilha_Encadeada()
    
    while True:
        menu = input('Digite a operação: \n1- Empilhar \n2- Remover pares \n3- Sair\n')

        if menu == '1':
            num = int(input('Digite o número a ser empilhado: '))
            pilha.empilhar(No(num))
        
        elif menu == '2':
            nova_pilha = Pilha_Encadeada()
            while not pilha.esta_vazia():
                valor = pilha.desempilhar()
                if valor.dado % 2 != 0:
                    nova_pilha.empilhar(No(valor))
            print(nova_pilha)
            while not nova_pilha.esta_vazia():
                pilha.empilhar(nova_pilha.desempilhar())
            print(pilha)
        
        elif menu == '3':
            break

        else:
            print('Operação Inválida')
            

