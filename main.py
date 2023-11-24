import os
from dotenv import load_dotenv
from cliente import Cliente
from EstoqueProduto import EstoqueProduto
from Caixa import Caixa

class Main():
    def menu():
        print("\t\t  Menu\n")
        opcao = int(input("1 - Estoque\t\t\t2 - Cliente\n3 - Caixa\t\t\t4 - Relatórios\n\t\t5 - Sair\n\n"))
        while opcao != 5:
            if opcao == 1:
                print("\n\n\t\t\t  Estoque\n")
                opcaoe = int(input("1 - Cadastrar produto\t\t\t2 - Consultar por nome\n3 - Alterar produto\t\t\t4 - Deletar produto\n\t\t\t5 - Voltar\n\n"))
                if opcaoe == 1: EstoqueProduto.cadastrar()
                elif opcaoe == 2: EstoqueProduto.consulta()
                elif opcaoe == 3: EstoqueProduto.alterar()
                elif opcaoe == 4: EstoqueProduto.deletar()
                elif opcaoe == 5: Main.menu()
                else: break
            elif opcao == 2:
                print("\n\n\t\t\t  Cliente\n")
                opcaoc = int(input("1 - Cadastrar cliente\t\t\t2 - Consultar por CPF\n3 - Alterar cliente\t\t\t4 - Deletar cliente\n\t\t\t5 - Voltar\n\n"))
                if opcaoc == 1: Cliente.cadastrar()
                elif opcaoc == 2: Cliente.consulta()
                elif opcaoc == 3: Cliente.alterar()
                elif opcaoc == 4: Cliente.deletar()
                elif opcaoc == 5: Main.menu()
                else: break
            elif opcao == 3:
                print("\n\n\t\t  Caixa \n")
                opcaocaixa = int(input("1 - Caixa\t\t\t2 - Venda\n\t\t3 - Voltar\n\n"))
                if opcaocaixa == 1: Caixa.exibir()
                elif opcaocaixa == 2: Caixa.venda()
                elif opcaocaixa == 3: Main.menu()
                else: break
            elif opcao == 4:
                print("\n\n\t\t\t  Relatórios\n")
                opcaor = int(input("1 - Produtos mais vendidos\t\t2 - Melhores compradores\n\t\t\t  3 - Voltar\n\n"))
                if opcaor == 1: EstoqueProduto.maisVendido()
                elif opcaor == 2: Cliente.melhorComprador()
                elif opcaor == 3: Main.menu()
                else: break
                
    def main():
        LOGIN={"login":"administrador","senha":"admin123"}
        print("\n\n\t\tFRUTIFICA\n\n")
        
        login = input("Login: ")
        senha = input("Senha: ")
        
        if(login == LOGIN['login'] and senha == LOGIN['senha']):
            print("Usuário logado!\n\n\n")
            Main.menu()
        else:
            print("Usuário e/ou senha incorreta!")
            Main.main()
            
Main.main()