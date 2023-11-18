class Cliente_produto:
    def __init__(self, cpf_cliente, idproduto, nomeproduto,preco_produto, tipo_produto):
        self.cpf_cliente = cpf_cliente
        self.idproduto = idproduto
        self.nomeproduto = nomeproduto
        self.preco_produto = preco_produto
        self.tipo_produto = tipo_produto

    def compra(self):
        self.cpf_cliente = int(input('Digite o CPF: '))
        self.idproduto = int(input('Qual o ID do produto? '))
        self.nomeproduto = input('Qual o nome do produto? ')
        self.preco_produto = float(input('Qual o valor do produto? '))
        self.tipo_produto = input('Qual o tipo do produto? ')
    