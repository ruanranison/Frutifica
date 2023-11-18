class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def cadastrar_produto(self):
        self.nome = input('Digite o nome do produto: ')
        self.quantidade = float(input('Digite a quantidade do produto: '))
        self.preco = float(input('Digite o valor do produto: R$ '))
        respostap = input(f'Para confirmar os dados, digite SIM, para REINICIAR, digite NAO \nNome: {self.nome} \nQuantidade: {self.quantidade} \nPreço: R${self.preco} \n')
            
        if respostap == 'SIM':
            print('Feto, coloque no arquivo')
        else:
            Produto.cadastrar_produto(self)
    
    def exibir_produto(self):
        print(f'Nome: {self.nome}, Quantidade: {self.quantidade}, Preço: R${self.preco} ')