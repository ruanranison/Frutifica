class Cliente:
    def __init__ (self, nome, idade, cpf, numero_telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.numero_telefone = numero_telefone

    def exibir(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, CPF: {self.idade}, Número de Telefone {self.numero_telefone}")
    
    def cadastrar(self):
        self.nome = input('Digite o nome do cliente: ')
        self.idade = int(input('Digite a idade do cliente: '))
        self.cpf = int(input('Digite o CPF do cliente: '))
        self.numero_telefone = int(input('Digite o número de telefone'))
        resposta = input(f'Os dados do novo cliente são (digite SIM para confirmar e NAO para reiniciar): \nNome: {self.nome},\nIdade: {self.idade},\nCPF: {self.idade},\nNúmero de Telefone:  {self.numero_telefone} \n')

        if resposta == "SIM":
            print('Feto, coloque no arquivo')
        else:
            Cliente.cadastrar(self)

    


