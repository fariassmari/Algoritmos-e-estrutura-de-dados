def selectionSort(tabela):
    for i in range(len(tabela)-1, 1, -1):
        maior = tabela[0]
        indice = 0

        for j in range(1, i+1):
            if tabela[j] > maior:
                maior = tabela[j]
                indice = j

        tabela[indice], tabela[i] = tabela[i], maior

def selectionSort2(tabela):
    for i in range(len(tabela)-1, 1, -1): # Percorre colocando o primeiro elemento como menor e pegando o indice dele
        menor = tabela[0]
        indice = 0

        for j in range(1, i+1): # Percorre o resto da tabela achando o menor elemento da tabela para ir para primeira posição e assim sucessivamente
            if tabela[j] < menor:
                menor = tabela[j]
                indice = j

        tabela[indice], tabela[i] = tabela[i], menor 