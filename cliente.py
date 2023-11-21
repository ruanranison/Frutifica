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
        idade = int(input('Digite a idade do cliente: '))
        cpf = input('Digite o CPF do cliente: ')
        numero_telefone = input('Digite o número de telefone: ')
        resposta = input(f'Os dados do novo cliente são (digite SIM para confirmar e NAO para reiniciar): \nNome: {nome},\nIdade: {idade},\nCPF: {cpf},\nNúmero de Telefone:  {numero_telefone} \n')

        if resposta == "SIM":
            c = open(os.getenv("Cliente"), "a")
            c.write("\n"+nome+","+str(idade)+","+cpf+","+numero_telefone)
            c.close()
            print("Cliente cadastrado!")
            
        else:
            Cliente.cadastrar()
            
    def consulta():
        realized = False
        lista = []
        arquivo = open(os.getenv("Cliente"), "r")
        c = arquivo.readlines()
        for i in c:
            cliente = i.replace("\n", "")
            lista.append(cliente)
        cpf_consulta = input('Digite o CPF do cliente para a consulta: ')
        for i in lista:
            if(cpf_consulta == i.split(",")[2]):
                nome, idade, cpf, numero_telefone = i.split(",")
                cliente = Cliente(nome=nome, idade=idade, cpf=cpf, numero_telefone=numero_telefone)
                cliente.exibir()
                realized = True
        if realized != True:
            print("Dados incorretos!")
            opcao = input("1 - Inserir dados novamente\n")
            if opcao == 1: Cliente.consulta()
            realized 
        arquivo.close()
        
    def deletar():
        realized = False
        arquivo = open(os.getenv("Cliente"), "r")
        cpf_consulta = input('Digite o CPF do cliente para deletar: ')
        c = arquivo.readlines()
        for i in c:
            if(cpf_consulta == i.split(",")[2]):
                c.remove(i)
                w = open(os.getenv("Cliente"), "w")
                w.writelines(c)
                print("Cliente deletado!\n")
                realized = True
        if realized != True:
            print("Dados incorretos!")
            opcao = input("1 - Inserir dados novamente\n")
            if opcao == 1: Cliente.deletar()        
        arquivo.close()
    
    def alterar():
        realized = False
        arquivo = open(os.getenv("Cliente"), "r")
        cpf_consulta = input('Digite o CPF do cliente para alterar: ')
        c = arquivo.readlines()
        for i in c:
            if(cpf_consulta == i.split(",")[2]):
                nome = input('Digite o nome do cliente: ')
                idade = int(input('Digite a idade do cliente: '))
                numero_telefone = input('Digite o número de telefone: ')
                resposta = input(f'Os dados do cliente são (digite SIM para confirmar e NAO para reiniciar): \nNome: {nome},\nIdade: {idade},\nCPF: {cpf_consulta},\nNúmero de Telefone:  {numero_telefone} \n')
                if resposta == "SIM":
                    c.remove(i)
                    alterado = "\n"+nome+","+str(idade)+","+cpf_consulta+","+numero_telefone
                    c.append(alterado)
                    w = open(os.getenv("Cliente"), "w")
                    w.writelines(c)
                    print("Cliente alterado!\n\n")
                    realized = True
                else:
                    Cliente.alterar()
                
        if realized != True:
            print("Dados incorretos!")
            opcao = input("1 - Inserir dados novamente\n")
            if opcao == 1: Cliente.alterar()     
        arquivo.close()        