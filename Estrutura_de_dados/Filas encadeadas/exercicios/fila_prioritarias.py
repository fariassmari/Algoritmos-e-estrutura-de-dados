from filas import No, Fila_Encadeada

if __name__ == '__main__':
    fila_normal = Fila_Encadeada()
    fila_prioritaria = Fila_Encadeada()

    while True:
        op = input('1- Adicionar Cliente \n2- Chamar cliente \n3- Mostrar Filas \n4- Sair \n')

        if op == '1':
            nome = input('Digite o nome do cliente: ')
            idade = int(input('Digite a idade do cliente: '))

            if idade >= 65:
                fila_prioritaria.adicionar(No(nome))
            else:
                fila_normal.adicionar(No(nome))
        elif op == '2':
            if not fila_prioritaria.esta_vazia():
                fila_prioritaria.remover()
            else: 
                fila_normal.remover()
        elif op == '3':
            print(fila_normal)
            print(fila_prioritaria)
        elif op == '4':
            break
        else:
            print('Operação Inválida')


        