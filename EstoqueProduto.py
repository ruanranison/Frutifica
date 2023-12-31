import os
from decouple import config
#from decouple import config

class EstoqueProduto:
    def __init__(self, nome, quantidade, preco, tipo, pontos):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.tipo = tipo
        self.pontos = pontos

    def exibir(self):
        print(f'Nome: {self.nome}\t Quantidade: {self.quantidade}\nPreço: R${self.preco}\t Tipo: {self.tipo} ')
        
    def cadastrar():
        nome = input('Digite o nome do produto: ')
        quantidade = int(input('Digite a quantidade do produto: '))
        preco = float(input('Digite o valor do produto: R$ '))
        tipo = input('Digite o tipo do produto: ')
        resposta = input(f'Para confirmar os dados, digite SIM, para REINICIAR, digite NAO \nNome: {nome} \nQuantidade: {quantidade} \nPreço: R${preco} \nTipo: {tipo}\n')
            
        if resposta == 'SIM':
            c = open(config("EstoqueProduto"), "a")
            c.write("\n"+nome+","+str(quantidade)+","+str(preco)+","+tipo+",0")
            c.close()
            print("Produto cadastrado!")
        else:
            EstoqueProduto.cadastrar()
    
    def consulta():
        realized = False
        lista = []
        arquivo = open(config("EstoqueProduto"), "r")
        c = arquivo.readlines()
        for i in c:
            cliente = i.replace("\n", "")
            lista.append(cliente)
        produto_consulta = input('Digite o nome do produto para a consulta: ')
        for i in lista:
            if(produto_consulta == i.split(",")[0]):
                nome, quantidade, preco, tipo, pontos = i.split(",")
                ep = EstoqueProduto(nome=nome, quantidade=quantidade, preco=preco, tipo=tipo, pontos=pontos)
                ep.exibir()
                realized = True
        if realized != True:
            print("Dados incorretos!")
            opcao = input("1 - Inserir dados novamente\n")
            if opcao == 1: EstoqueProduto.consulta() 
        arquivo.close()
            
    def deletar():
        realized = False
        arquivo = open(config("EstoqueProduto"), "r")
        c = arquivo.readlines()
        nome_consulta = input('Digite o nome do produto para deletar: ')
        for i in c:
            if(nome_consulta == i.split(",")[0]):
                c.remove(i)
                w = open(config("EstoqueProduto"), "w")
                w.writelines(c)
                print("Produto deletado!\n")
                realized = True
        if realized != True:
            print("Dados incorretos!")
            opcao = input("1 - Inserir dados novamente\n")
            if opcao == 1: EstoqueProduto.deletar() 
        arquivo.close()        
    
    def alterar():
        realized = False
        arquivo = open(config("EstoqueProduto"), "r")
        c = arquivo.readlines()
        nome_consulta = input('Digite o nome do produto para alterar: ')
        for i in c:
            if(i != "\n"):
                if(nome_consulta == i.split(",")[0]):
                    pontos = i.split(",")[4]
                    nome = input('Digite o nome do produto: ')
                    quantidade = int(input('Digite a quantidade do produto: '))
                    preco = float(input('Digite o valor do produto: R$ '))
                    tipo = input('Digite o tipo do produto: ')
                    resposta = input(f'Para confirmar os dados, digite SIM, para REINICIAR, digite NAO \nNome: {nome} \nQuantidade: {quantidade} \nPreço: R${preco} \nTipo: {tipo}\n')
                    if resposta == "SIM":
                        alterado = "\n"+nome+","+str(quantidade)+","+str(preco)+","+tipo+","+pontos
                        c.append(alterado)
                        c.remove(i)
                        w = open(config("EstoqueProduto"), "w")
                        w.writelines(c)
                        arquivo.close()
                        w.close()
                        print("Produto alterado!\n\n")
                        realized = True
                    else:
                        EstoqueProduto.alterar()      
        
        if realized != True:
            print("Dados incorretos!")
            opcao = int(input("1 - Inserir dados novamente\t2 - Sair\n"))
            if opcao == 1: EstoqueProduto.alterar() 
    
    def maisVendido():
        maisVendido = []
        arquivo = open(config("EstoqueProduto"), "r")
        c = arquivo.readlines()
        for i in c:
            if(i != "\n"):
                maisVendido.append(i)
        maisVendido = sorted(maisVendido, key=lambda x: x.split(",")[4], reverse=True)
        arquivo.close()
        print("\n\n\t\t\t  Produtos mais vendidos\n")
        for index, i in enumerate(maisVendido):
            print(str(index + 1)+" - "+i.split(",")[0])
        print("\n\n")