import os
from dotenv import load_dotenv
from Cliente import Cliente
from ClienteProduto import ClienteProduto
from Caixa import Caixa

load_dotenv()

class EstoqueProduto:
    def __init__(self, nome, quantidade, preco, tipo):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.tipo = tipo

    def exibir(self):
        print(f'Nome: {self.nome}\t Quantidade: {self.quantidade}\nPreço: R${self.preco}\t Tipo: {self.tipo} ')
        
    def cadastrar():
        nome = input('Digite o nome do produto: ')
        quantidade = int(input('Digite a quantidade do produto: '))
        preco = float(input('Digite o valor do produto: R$ '))
        tipo = input('Digite o tipo do produto: ')
        resposta = input(f'Para confirmar os dados, digite SIM, para REINICIAR, digite NAO \nNome: {nome} \nQuantidade: {quantidade} \nPreço: R${preco} \nTipo: {tipo}\n')
            
        if resposta == 'SIM':
            c = open(os.getenv("EstoqueProduto"), "a")
            c.write("\n"+nome+","+str(quantidade)+","+str(preco)+","+tipo)
            c.close()
            print("Produto cadastrado!")
        else:
            EstoqueProduto.cadastrar()
    
    def consulta():
        realized = False
        lista = []
        arquivo = open(os.getenv("EstoqueProduto"), "r")
        c = arquivo.readlines()
        for i in c:
            cliente = i.replace("\n", "")
            lista.append(cliente)
        produto_consulta = input('Digite o nome do produto para a consulta: ')
        for i in lista:
            if(produto_consulta == i.split(",")[0]):
                nome, quantidade, preco, tipo = i.split(",")
                ep = EstoqueProduto(nome=nome, quantidade=quantidade, preco=preco, tipo=tipo)
                ep.exibir()
                realized = True
        if realized != True:
            print("Dados incorretos!")
            opcao = input("1 - Inserir dados novamente\n")
            if opcao == 1: EstoqueProduto.consulta() 
        arquivo.close()
            
    def venda():
        realized = False
        arquivo = open(os.getenv("EstoqueProduto"), "r")
        c = arquivo.readlines()
        produto_venda = input('Digite o nome do produto para a venda: ')
        for i in c:
            if(produto_venda == i.split(",")[0]):
                nome_produto, quantidade, preco, tipo = i.split(",")
                quantidade = int(quantidade)
                quantidade_venda = int(input('Digite a quantidade do produto para a venda: '))
                if quantidade_venda <= quantidade:
                    listaj = []
                    arquivoj = open(os.getenv("Cliente"), "r")
                    cj = arquivoj.readlines()
                    for j in cj:
                        cliente = j.replace("\n", "")
                        listaj.append(cliente)
                    cpf_consulta = input('Digite o CPF do cliente para a consulta: ')
                    for j in listaj:
                        if(cpf_consulta == j.split(",")[2]):
                            cpf = j.split(",")[2]
                            alterado = "\n"+nome_produto+","+str((quantidade-quantidade_venda))+","+preco+","+tipo
                            c.append(alterado)
                            c.remove(i)
                            w = open(os.getenv("EstoqueProduto"), "w")
                            w.writelines(c)
                            cp = ClienteProduto(cpf_cliente=cpf, nome_produto=nome_produto, preco_produto=preco, tipo_produto=tipo, quantidade_venda=quantidade_venda)
                            cp.venda()
                            Caixa.adicionar(float(quantidade_venda)*float(preco))
                            realized = True
                    if realized != True:
                        print("Dados incorretos!")
                        opcao = input("1 - Inserir dados novamente\n")
                        if opcao == 1: Cliente.consulta()
                else: 
                    print("Quantidade de estoque insuficiente!\n"+nome_produto+" possui "+str(quantidade)+" unidades no estoque.")
                    opcao = input("1 - Menu\t2 - Inserir dados novamente\n")
                    if opcao == 1: 
                        break
                    else: 
                        EstoqueProduto.venda()    
        if realized != True:
            print("Dados incorretos!")
            opcao = input("1 - Inserir dados novamente\n")
            if opcao == 1: EstoqueProduto.venda() 
        arquivo.close()
            
    def deletar():
        realized = False
        arquivo = open(os.getenv("EstoqueProduto"), "r")
        c = arquivo.readlines()
        nome_consulta = input('Digite o nome do produto para deletar: ')
        for i in c:
            if(nome_consulta == i.split(",")[0]):
                c.remove(i)
                w = open(os.getenv("EstoqueProduto"), "w")
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
        arquivo = open(os.getenv("EstoqueProduto"), "r")
        c = arquivo.readlines()
        nome_consulta = input('Digite o nome do produto para alterar: ')
        for i in c:
            if(nome_consulta == i.split(",")[0]):
                nome = input('Digite o nome do produto: ')
                quantidade = int(input('Digite a quantidade do produto: '))
                preco = float(input('Digite o valor do produto: R$ '))
                tipo = input('Digite o tipo do produto: ')
                resposta = input(f'Para confirmar os dados, digite SIM, para REINICIAR, digite NAO \nNome: {nome} \nQuantidade: {quantidade} \nPreço: R${preco} \nTipo: {tipo}\n')
                if resposta == "SIM":
                    alterado = "\n"+nome+","+str(quantidade)+","+str(preco)+","+tipo
                    c.append(alterado)
                    c.remove(i)
                    w = open(os.getenv("EstoqueProduto"), "w")
                    w.writelines(c)
                    print("Produto alterado!\n\n")
                    realized = True
                else:
                    EstoqueProduto.alterar()
                
        if realized != True:
            print("Dados incorretos!")
            opcao = input("1 - Inserir dados novamente\n")
            if opcao == 1: EstoqueProduto.alterar() 
        arquivo.close()
    