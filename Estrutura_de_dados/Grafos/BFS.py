def breadth_first_search(self, inicio):
    visitado = []
    fila = []
    saida = []

    fila.append(inicio)
    visitado.append(inicio)

    while fila != []:
        atual = fila.pop(0)
        saida.append(atual.dado)

        for edge in atual.adj:
            neighbor = edge.destino

            if neighbor not in visitado:
                visitado.append(neighbor)
                fila.append(neighbor)
    return saida