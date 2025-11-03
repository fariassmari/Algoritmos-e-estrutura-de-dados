from pilhas import No, Pilha_Encadeada

if __name__ == '__main__':
    verificar = Pilha_Encadeada()

    expressao = input('Digite a expressão: ')

    simbolos_abertura = '([{'
    simbolos_fechamento = ')]}'
    correspondencia = {')':'(', ']':'[', '}':'{'}

    for c in expressao:
        if c in simbolos_abertura:
            verificar.empilhar(No(c))
        elif c in simbolos_fechamento:
            if verificar.esta_vazia():
                print(False)
                break
            topo = verificar.desempilhar()
            if topo.dado != correspondencia[c]:
                print(False)
                break
        else:
            print(verificar.esta_vazia())
