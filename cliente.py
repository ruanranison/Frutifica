import os
from dotenv import load_dotenv

load_dotenv()

class Cliente:
    def __init__ (self, nome, idade, cpf, numero_telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.numero_telefone = numero_telefone

    def exibir(self):
        print(f"\nNome: {self.nome}\tIdade: {self.idade}\nCPF: {self.cpf}\t\tNúmero de Telefone: {self.numero_telefone}\n\n")
    
    def cadastrar():
        nome = input('Digite o nome do cliente: ')
        idade = input('Digite a idade do cliente: ')
        cpf = input('Digite o CPF do cliente: ')
        numero_telefone = input('Digite o número de telefone: ')
        resposta = input(f'Os dados do novo cliente são (digite SIM para confirmar e NAO para reiniciar): \nNome: {nome},\nIdade: {idade},\nCPF: {cpf},\nNúmero de Telefone:  {numero_telefone} \n')

        if resposta == "SIM":
            c = open(os.getenv("Cliente"), "a")
            c.write("\n"+nome+","+idade+","+cpf+","+numero_telefone)
            c.close()
            print("Cliente cadastrado!")
            
        else:
            Cliente.cadastrar()
            
    def consulta():
        lista = []
        c = open(os.getenv("Cliente"), "r")
        for i in c:
            cliente = i.replace("\n", "")
            lista.append(cliente)
        cpf_consulta = input('Digite o CPF do cliente para a consulta: ')
        for i in lista:
            if(cpf_consulta == i.split(",")[2]):
                nome, idade, cpf, numero_telefone = i.split(",")
                cliente = Cliente(nome=nome, idade=idade, cpf=cpf, numero_telefone=numero_telefone)
                cliente.exibir()
            else:
                print("Dados incorretos!")
                opcao = input("1 - Menu\t2 - Inserir dados novamente")
                if opcao == 1: 
                    break
                else: 
                    Cliente.consulta()
        c.close()
        
    def deletar():
        c = open(os.getenv("Cliente"), "r")
        cpf_consulta = input('Digite o CPF do cliente para a consulta: ')
        c = c.readlines()
        for i in c:
            if(cpf_consulta == i.split(",")[2]):
                c.remove(i)
                w = open(os.getenv("Cliente"), "w")
                w.writelines(c)
                print("Cliente deletado!\n")
            else:
                print("Dados incorretos!")
                opcao = input("1 - Menu\t2 - Inserir dados novamente")
                if opcao == 1: 
                    break
                else: 
                    Cliente.deletar()
        w.close()        
    
    def alterar():
        c = open(os.getenv("Cliente"), "r")
        cpf_consulta = input('Digite o CPF do cliente para a consulta: ')
        c = c.readlines()
        for i in c:
            if(cpf_consulta == i.split(",")[2]):
                nome = input('Digite o nome do cliente: ')
                idade = input('Digite a idade do cliente: ')
                numero_telefone = input('Digite o número de telefone: ')
                resposta = input(f'Os dados do cliente são (digite SIM para confirmar e NAO para reiniciar): \nNome: {nome},\nIdade: {idade},\nCPF: {cpf_consulta},\nNúmero de Telefone:  {numero_telefone} \n')
                if resposta == "SIM":
                    c.remove(i)
                    alterado = nome+","+idade+","+cpf_consulta+","+numero_telefone
                    c.append(alterado)
                    w = open(os.getenv("Cliente"), "w")
                    w.writelines(c)
                    print("Cliente alterado!\n\n")
                else:
                    Cliente.alterar()
                
            else:
                print("Dados incorretos!")
                opcao = input("1 - Menu\t2 - Inserir dados novamente")
                if opcao == 1: 
                    break
                else: 
                    Cliente.alterar()
        w.close()        