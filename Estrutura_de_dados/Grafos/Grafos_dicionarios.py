class Vertice: # Cria o vértice
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = {}

    def adicionar_vizinho(self, vertice, peso=1): # Adiciona o vizinho com seu determinado peso
        self.vizinhos[vertice] = peso

    def __repr__(self):
        return f"Vertice({self.nome})"
    
class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def adicionar_vertices(self, nome): # Se o vertice nao existir ele é criado 
        if nome not in self.vertices:
            self.vertices[nome] = Vertice(nome)

    def adicionar_aresta(self, origem, destino, peso=1): # Verifica se o vertices origem e destino existem pra poder ligar ele  
        if origem not in self.vertices:
            self.adicionar_vertices(origem)

        if destino not in self.vertices:
            self.adicionar_vertices(destino)

        self.vertices[origem].adicionar_vizinho(self.vertices[destino], peso)
        self.vertices[destino].adicionar_vizinho(self.vertices[origem], peso)

    def mostrar_grafo(self): # Mostra o grafo
        for nome, vertice in self.vertices.items():
            vizinhos = []

            for v, p in vertice.vizinhos.items():
                vizinhos.append(f'{v.nome} (peso={p})')

            print(f'{nome} -> {vizinhos}')    

if __name__ == "__main__":
    grafo = Grafo()

    grafo.adicionar_aresta("A", "B")
    grafo.adicionar_aresta("A", "F")

    grafo.adicionar_aresta("B", "C")
    grafo.adicionar_aresta("B", "D")
    grafo.adicionar_aresta("B", "F")

    grafo.adicionar_aresta("C", "D")
    grafo.adicionar_aresta("C", "F")

    grafo.adicionar_aresta("D", "E")
    grafo.adicionar_aresta("D", "F")
    
    grafo.adicionar_aresta("E", "F")

    grafo.mostrar_grafo()