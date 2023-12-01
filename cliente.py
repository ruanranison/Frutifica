from decouple import config

class Cliente:
    def __init__ (self, nome, idade, cpf, numero_telefone, pontos):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.numero_telefone = numero_telefone
        self.pontos = pontos

    def exibir(self):
        print(f"\nNome: {self.nome}\tIdade: {self.idade}\nCPF: {self.cpf}\t\tNúmero de Telefone: {self.numero_telefone}\n\n")
    
    def cadastrar():
        nome = input('Digite o nome do cliente: ')
        idade = int(input('Digite a idade do cliente: '))
        cpf = input('Digite o CPF do cliente: ')
        numero_telefone = input('Digite o número de telefone: ')
        resposta = input(f'Os dados do novo cliente são (digite SIM para confirmar e NAO para reiniciar): \nNome: {nome},\nIdade: {idade},\nCPF: {cpf},\nNúmero de Telefone:  {numero_telefone} \n')

        if resposta == "SIM":
            c = open(config("Cliente"), "a")
            c.write("\n"+nome+","+str(idade)+","+cpf+","+numero_telefone+",0")
            c.close()
            print("Cliente cadastrado!")
            
        else:
            Cliente.cadastrar()
            
    def consulta():
        realized = False
        lista = []
        arquivo = open(config("Cliente"), "r")
        c = arquivo.readlines()
        for i in c:
            cliente = i.replace("\n", "")
            lista.append(cliente)
        cpf_consulta = input('Digite o CPF do cliente para a consulta: ')
        for i in lista:
            if(i != "\n" and i != ''):
                if(cpf_consulta == i.split(",")[2]):
                    nome, idade, cpf, numero_telefone, pontos = i.split(",")
                    cliente = Cliente(nome=nome, idade=idade, cpf=cpf, numero_telefone=numero_telefone, pontos=pontos)
                    cliente.exibir()
                    realized = True
        if realized != True:
            print("Dados incorretos!")
            opcao = int(input("1 - Inserir dados novamente\t2 - Sair\n"))
            if opcao == 1: 
                Cliente.consulta()
        arquivo.close()
        
    def deletar():
        realized = False
        arquivo = open(config("Cliente"), "r")
        cpf_consulta = input('Digite o CPF do cliente para deletar: ')
        c = arquivo.readlines()
        for i in c:
            if(i != "\n"):
                if(cpf_consulta == i.split(",")[2]):
                    c.remove(i)
                    w = open(config("Cliente"), "w")
                    w.writelines(c)
                    print("Cliente deletado!\n")
                    realized = True
        if realized != True:
            print("Dados incorretos!")
            opcao = int(input("1 - Inserir dados novamente\n"))
            if opcao == 1: Cliente.deletar()        
        arquivo.close()
    
    def alterar():
        realized = False
        arquivo = open(config("Cliente"), "r")
        cpf_consulta = input('Digite o CPF do cliente para alterar: ')
        c = arquivo.readlines()
        for i in c:
            if(i != "\n"): 
                if(cpf_consulta == i.split(",")[2]):
                    nome = input('Digite o nome do cliente: ')
                    idade = int(input('Digite a idade do cliente: '))
                    numero_telefone = input('Digite o número de telefone: ')
                    pontos = i.split(",")[4]
                    resposta = input(f'Os dados do cliente são (digite SIM para confirmar e NAO para reiniciar): \nNome: {nome},\nIdade: {idade},\nCPF: {cpf_consulta},\nNúmero de Telefone:  {numero_telefone} \n')
                    if resposta == "SIM":
                        alterado = "\n"+nome+","+str(idade)+","+cpf_consulta+","+numero_telefone+","+pontos
                        c.append(alterado)
                        c.remove(i)
                        w = open(config("Cliente"), "w")
                        w.writelines(c)
                        print("Cliente alterado!\n\n")
                        realized = True
                    else:
                        Cliente.alterar()
        
        arquivo.close()     
        if realized != True:
            print("Dados incorretos!")
            opcao = int(input("1 - Inserir dados novamente\n"))
            if opcao == 1: Cliente.alterar()     
        
    def pontuacao(cpf_consulta, valor):
        valor = int(valor)
        arquivo = open(config("Cliente"), "r")
        c = arquivo.readlines()
        for i in c:
            if(i != "\n"):
                if(cpf_consulta == i.split(",")[2]):
                    nome, idade, cpf, numero_telefone, pontos = i.split(",")
                    pontos = int(pontos) + (valor * 5)
                    c.remove(i)
                    alterado = "\n"+nome+","+str(idade)+","+cpf+","+numero_telefone+","+str(pontos)
                    c.append(alterado)
                    w = open(config("Cliente"), "w")
                    w.writelines(c)   
            
        arquivo = open(config("EstoqueProduto"), "r")
        c = arquivo.readlines()
        for i in c:
            if(cpf_consulta == i.split(",")[2]):
                nome, quantidade, preco, tipo, pontos = i.split(",")
                pontos = int(pontos) + (valor * 5)
                c.remove(i)
                alterado = "\n"+nome+","+str(idade)+","+cpf+","+numero_telefone+","+str(pontos)
                c.append(alterado)
                w = open(config("EstoqueProduto"), "w")
                w.writelines(c)   
        arquivo.close()
        
    def melhorComprador():
        melhorComprador = []
        arquivo = open(config("Cliente"), "r")
        c = arquivo.readlines()
        for i in c:
            if(i != "\n"):
                melhorComprador.append(i)
        melhorComprador = sorted(melhorComprador, key=lambda x: x.split(",")[4], reverse=True)
        arquivo.close()
        print("\n\n\t\t\t  Melhores compradores\n")
        for index, i in enumerate(melhorComprador):
            print(str(index + 1)+"º - "+i.split(",")[0])
        print("\n\n")