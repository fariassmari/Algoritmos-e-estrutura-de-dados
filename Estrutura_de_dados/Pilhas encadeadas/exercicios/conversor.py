from pilhas import No, Pilha_Encadeada

if __name__ == '__main__':
    conversor = Pilha_Encadeada()

    numero = int(input('Digite o número: '))

    resultado = ''

    while numero >= 1:
        restos = numero % 2
        conversor.empilhar(No(restos))
        numero =  numero // 2

    while not conversor.esta_vazia():
        no = conversor.desempilhar()
        resultado += str(no.dado)

    print(resultado)

    