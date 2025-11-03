from filas import No, Fila_Encadeada

if __name__ == '__main__':
    fila = Fila_Encadeada()

    while True:
        op = input('1- Adicionar documento \n2- Imprimir \n3- Exibir Fila \n4- Sair\n')

        if op == '1':
            nome = input('Digite o nome do documento')
            fila.adicionar(No(nome))

        elif op == '2':
            fila.remover()

        elif op == '3':
            print(fila)
        
        elif op == '4':
            break

        else:
            print('Operação Inválida')