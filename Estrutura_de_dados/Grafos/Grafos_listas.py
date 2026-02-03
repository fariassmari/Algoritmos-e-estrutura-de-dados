class Aresta():
    def __init__(self, origem, destino, peso):
        self.__origem = origem
        self.__destino = destino
        self.__peso = peso

    @property
    def origem(self):
        return self.__origem
    @property
    def destino(self):
        return self.__destino
    @property
    def peso(self):
        return self.__peso
    
    @origem.setter
    def origem(self, novaOrigem):
        self.__origem = novaOrigem
    @destino.setter
    def destino(self, novoDestino):
        self.__destino = novoDestino
    @peso.setter
    def peso(self, novoPeso):
        self.__peso = novoPeso

    def __str__(self):
        return f'{self.__origem}, {self.__destino}, {self.__peso}'
    
class Vertice():
    def __init__(self, dado):
        self.__dado = dado
        self.__adj = [] # Vertices que se ligam pela aresta

    def addAdj(self, edge):
        self.__adj.append(edge)

    @property
    def dado(self):
        return self.__dado

    @dado.setter
    def dado(self, dado):
        self.__dado = dado

    @property
    def adj(self):
        return self.__adj

    def __str__(self):
        return self.__dado
    
class Grafo():
    def __init__(self):
        self.__vertices = [] 
        self.__arestas = []
    
    @property
    def vertices(self):
        return self.__vertices

    @vertices.setter
    def vertices(self, novoVertice):
        self.__vertices = novoVertice

    @property
    def arestas(self):
        return self.__arestas

    @arestas.setter
    def arestas(self, novaAresta):
        self.__arestas = novaAresta

    def addVertice(self, nome):
        v = Vertice(nome)
        self.__vertices.append(v)
        return v
    
    def addAresta(self, origem, destino, peso):
        a = Aresta(origem, destino, peso)
        origem.addAdj(a)
        self.__arestas.append(a)
        return a
    
    def getNumVertices(self):
        return len(self.__vertices)
    
    def getNumArestas(self):
        return len(self.__arestas)

    def breadth_first_search(self, inicio):
        visitado = [] # Guarda os vertices ja visitados 
        fila = [] # Fila controla a visita 
        saida = [] # Armazena a ordem final

        fila.append(inicio) # Primeiro vértice entra na fila 
        visitado.append(inicio) # Se torna o visitado

        while fila != []:
            atual = fila.pop(0) # Remove o primeiro elemento da fila
            saida.append(atual.dado) # Guarda o valor do vertice que saiu da fila

            for edge in atual.adj: # Percorre os vizinhos do atual
                neighbor = edge.destino # Vertice vizinho
 
                if neighbor not in visitado: # Se o vertice vizinho nao tiver sido visitado entra na fila
                    visitado.append(neighbor)
                    fila.append(neighbor)
        return saida # Retorna a fila final

    def bfs_dist(self, inicio):
        visitado = [] # Guarda os vertices ja visitados 
        fila = [] # Fila controla a visita 
        saida = [] # Armazena a ordem final
        dist = {} 

        fila.append(inicio) # Primeiro vértice entra na fila 
        visitado.append(inicio) # Se torna o visitado
        dist[inicio] = 0

        while fila != []:
            atual = fila.pop(0) # Remove o primeiro elemento da fila
            saida.append(atual.dado) # Guarda o valor do vertice que saiu da fila

            for edge in atual.adj: # Percorre os vizinhos do atual
                neighbor = edge.destino # Vertice vizinho
 
                if neighbor not in visitado: # Se o vertice vizinho nao tiver sido visitado entra na fila
                    visitado.append(neighbor)
                    fila.append(neighbor)
                    dist[neighbor] = dist[atual] + 1
        return saida # Retorna a fila final
    
    def bfs_rec(self, fila, visitado, saida):
        if not fila:
            return
        atual = fila.pop(0)
        saida.append(atual.dado)

        for edge in atual.adj:
            neighbor = edge.destino
            if neighbor not in visitado:
                visitado.append(neighbor)
                fila.append(neighbor)
        return self.bfs_rec(fila, visitado, saida)
    
    def depth_first_search(self, inicio):
        visitado = []
        pilha = []
        saida = []

        pilha.insert(0, inicio)

        while pilha != []:
            atual = pilha.pop()
            
            if atual not in visitado:
                visitado.append(atual)
                saida.append(atual.dado)

                for edge in reversed(atual.adj):
                    vizinho = edge.destino
                    if vizinho not in visitado:
                        pilha.append(vizinho)
        return saida
    
    def dfs_rec(self, vertice, visitado, saida):
        if vertice in visitado:
            return

        visitado.append(vertice)
        saida.append(vertice.dado)

        for edge in vertice.adj:
            vizinho = edge.destino
            if vizinho not in visitado:
                self.dfs_rec(vertice, visitado, saida)
    
    def __str__(self):
        r = ''
        for u in self.__vertices:
            if len(u.adj) == 0:
                continue

            r += (str(u.dado) + ' -> ')

            for e in u.adj:
                v = e.destino
                r += v.dado + ', '
            r += '\n'
        return r
    
if __name__ == '__main__':
    g = Grafo()

    um = g.addVertice('1')
    dois = g.addVertice('2')
    tres = g.addVertice('3')
    quatro = g.addVertice('4')
    cinco = g.addVertice('5')

    print(f'Vertices: {g.getNumVertices()}, Arestas: {g.getNumArestas()}')

    g.addAresta(um, dois, 1)
    g.addAresta(um, tres, 1)
    g.addAresta(um, quatro, 1)
    g.addAresta(um, cinco, 1)

    print(f'Vertices: {g.getNumVertices()}, Arestas: {g.getNumArestas()}')
    print(g)

    g.addAresta(tres, dois, 1)
    g.addAresta(tres, quatro, 1)
    g.addAresta(tres, cinco, 1)

    print(f'Vertices: {g.getNumVertices()}, Arestas: {g.getNumArestas()}')
    print(g)

    '''g = Grafo()

    a = g.addVertice('a')
    b = g.addVertice('b')
    c = g.addVertice('c')
    d = g.addVertice('d')
    e = g.addVertice('e')
    f = g.addVertice('f')

    print(f'Vertices: {g.getNumVertices()}, Arestas: {g.getNumArestas()}')

    g.addAresta(a, b, 1)
    g.addAresta(a, f, 1)
    
    print(f'Vertices: {g.getNumVertices()}, Arestas: {g.getNumArestas()}')
    print(g)

    g.addAresta(b, a, 1)
    g.addAresta(b, c, 1)
    g.addAresta(b, d, 1)
    g.addAresta(b, f, 1)

    print(f'Vertices: {g.getNumVertices()}, Arestas: {g.getNumArestas()}')
    print(g)

    g.addAresta(c, b, 1)
    g.addAresta(c, d, 1)
    g.addAresta(c, f, 1)
    
    print(f'Vertices: {g.getNumVertices()}, Arestas: {g.getNumArestas()}')
    print(g)

    g.addAresta(d, b, 1)
    g.addAresta(d, c, 1)
    g.addAresta(d, e, 1)
    g.addAresta(d, f, 1)
    
    print(f'Vertices: {g.getNumVertices()}, Arestas: {g.getNumArestas()}')
    print(g)

    g.addAresta(e, d, 1)
    g.addAresta(e, f, 1)
    
    print(f'Vertices: {g.getNumVertices()}, Arestas: {g.getNumArestas()}')
    print(g)

    g.addAresta(f, a, 1)
    g.addAresta(f, b, 1)
    g.addAresta(f, c, 1)
    g.addAresta(f, d, 1)
    g.addAresta(f, e, 1)
    
    print(f'Vertices: {g.getNumVertices()}, Arestas: {g.getNumArestas()}')
    print(g)'''


    '''g = Grafo()

    print(f'Vertices: {g.getNumVertices()}, Arestas: {g.getNumArestas()}')

    maria = g.addVertice('Maria')
    lucia = g.addVertice('Lúcia')

    print(f'Vertices: {g.getNumVertices()}, Arestas: {g.getNumArestas()}')

    wilma = g.addVertice('Wilma')
    cleber = g.addVertice('Cleber')

    print(f'Vertices: {g.getNumVertices()}, Arestas: {g.getNumArestas()}')

    g.addAresta(maria, wilma, 2)
    g.addAresta(lucia, cleber, 2)

    print(g)
    print(f'Vertices: {g.getNumVertices()}, Arestas: {g.getNumArestas()}')

    mariana = g.addVertice('Mariana')

    g.addAresta(maria, mariana, 1)
    g.addAresta(lucia, mariana, 1)

    print(g)
    print(f'Vertices: {g.getNumVertices()}, Arestas: {g.getNumArestas()}')

    g.addAresta(wilma, mariana, 2)
    g.addAresta(cleber, mariana, 2)

    print(g)
    print(f'Vertices: {g.getNumVertices()}, Arestas: {g.getNumArestas()}')'''

    