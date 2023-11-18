class Produto:
    def __init__(self, nome, quantidade, preco, tipo):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.tipo = tipo

    def cadastrar_produto(self):
        self.nome = input('Digite o nome do produto: ')
        self.quantidade = float(input('Digite a quantidade do produto: '))
        self.preco = float(input('Digite o valor do produto: R$ '))
        self.tipo = input('Digite o tipo do produto: ')
        respostap = input(f'Para confirmar os dados, digite SIM, para REINICIAR, digite NAO \nNome: {self.nome} \nQuantidade: {self.quantidade} \nPreço: R${self.preco} \nTipo: {self.tipo} \n')
            
        if respostap == 'SIM':
            print('Feto, coloque no arquivo')
        else:
            Produto.cadastrar_produto(self)
    
    def exibir_produto(self):
        print(f'Nome: {self.nome}, Quantidade: {self.quantidade}, Preço: R${self.preco}, Tipo: {self.tipo} ')