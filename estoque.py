class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"Produto: {self.nome}, Quantidade: {self.quantidade}, Preço: {self.preco}"
    
class Estoque:
    def __init__(self):
        self.produtos = []

    def add_produto(self, produto):
        self.produtos.append(produto)

    def exibir_estoque(self):
        for produto in self.produtos:
            print(produto)
