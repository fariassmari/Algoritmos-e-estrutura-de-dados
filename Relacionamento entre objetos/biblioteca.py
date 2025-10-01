class Biblioteca:
    def __init__(self):
        self.__biblioteca = []
    
    def adicionar_livro(self, novo_livro):
        return self.__biblioteca.append(novo_livro)
    
    def remover_livro(self, livro):
        for i, l in enumerate(self.__livros):
            if self.__livro == livro:
                return self.__biblioteca.pop(i)

        

class Livro:
    def __init__(self, nome, autor, ano):
        self.__nome = nome
        self.__autor = autor
        self.__ano = ano

    @property
    def nome(self):
        return self.__nome
    @property
    def autor(self):
        return self.__autor
    @property
    def ano(self):
        return self.__ano
            


    