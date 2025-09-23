class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto):
        self.itens.append(produto)
        return produto
    
    def total(self):
        total = 0
        for item in self.itens:
            total += item.preco
        return total

produto1 = Produto('batata', 1.50)
produto2 = Produto('feijão', 3.50)
produto3 = Produto('cuzcuz', 2.80)

carrinho1 = Carrinho()

carrinho1.adicionar_produto(produto1)
carrinho1.adicionar_produto(produto2)
carrinho1.adicionar_produto(produto3)

print(carrinho1.total())
print(produto1.nome)