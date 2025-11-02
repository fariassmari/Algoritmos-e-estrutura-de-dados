class Produto:
    # Método construtor
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    # Método GET
    @property
    def nome(self):
        return self.__nome
    @property
    def preco(self):
        return self.__preco
    
    # Método SET
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    @preco.setter
    def preco(self, valor):
        self.__preco = valor

    def __str__(self):
        return f'Produto: {self.__nome}, Preço: {self.__preco}'
    

class Carrinho:
    def __init__(self):
        self.__itens = []

    def adicionar_produto(self, produto):
        self.__itens.append(produto)
        return produto
    
    def total(self):
        total = 0
        for item in self.__itens:
            total += item.preco
        return total
    
    def remover_produto(self, procurar_nome):
        for i, item in enumerate(self.__itens):
            if item.nome == procurar_nome:
                return self.__itens.pop(i)
        return None

    def __str__(self):
        if not self.__itens:
            return 'Carrinho vazio'
        else:
            resultado = 'Carrinho:\n'
            for item in self.__itens:
                resultado += str(item) + '\n'
            return f'Total do carrinho: {self.total():.2f} \n {resultado}'
    

if __name__ == "__main__":
    produto1 = Produto('batata', 1.50)
    produto2 = Produto('feijão', 3.50)
    produto3 = Produto('cuzcuz', 2.80)
    produto4 = Produto('tomate', 1.25)
    produto5 = Produto('macarrão', 2.23)
    produto6 = Produto('arroz', 3.23)

    carrinho1 = Carrinho()

    carrinho1.adicionar_produto(produto1)
    carrinho1.adicionar_produto(produto2)
    carrinho1.adicionar_produto(produto3)
    carrinho1.adicionar_produto(produto4)
    carrinho1.adicionar_produto(produto5)
    carrinho1.adicionar_produto(produto6)

    print(carrinho1)

    carrinho1.remover_produto('batata')
    print(carrinho1)