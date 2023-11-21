import os
from dotenv import load_dotenv
from Cliente import Cliente
from EstoqueProduto import EstoqueProduto
from Caixa import Caixa

load_dotenv()
class Main():
    def menu():
        print("\t\t  Menu\n")
        opcao = int(input("1 - Estoque\t\t\t2 - Cliente\n3 - Caixa\t\t\t4 - Relatórios\n\t\t5 - Sair\n\n"))
        while opcao != 5:
            if opcao == 1:
                print("\n\n\t\t\t  Estoque\n")
                opcaoe = int(input("1 - Cadastrar produto\t\t\t2 - Consultar por nome\n3 - Alterar produto\t\t\t4 - Deletar produto\n5 - Venda\t\t\t\t6 - Voltar\n\n"))
                if opcaoe == 1: EstoqueProduto.cadastrar()
                elif opcaoe == 2: EstoqueProduto.consulta()
                elif opcaoe == 3: EstoqueProduto.alterar()
                elif opcaoe == 4: EstoqueProduto.deletar()
                elif opcaoe == 5: EstoqueProduto.venda()
                elif opcaoe == 6: Main.menu()
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
                print("\n\n\t\t\t  Caixa\n")
                Caixa.exibir
                break
            elif opcao == 4:
                # menu relatorios
                break
    def main():
        print("\n\n\t\tFRUTIFICA\n\n")
        login = input("Login: ")
        senha = input("Senha: ")

        if(login == os.getenv("ADMIN") and senha == os.getenv("SENHA")):
            print("Usuário logado!\n\n\n")
            Main.menu()
        else:
            print("Usuário e/ou senha incorreta!")
            Main.main()
            
Main.main()


# adicionar produto no estoque, 
# venda do produto (consulta e retirada do produto) 
# deletar produto do estoque,
# alterar produto,

# adição de cliente, 
# consulta de cliente, 
# exclusão de cliente,
# alteração de cliente,

# adição ao caixa,
# retirada do caixa,

# produtos mais vendidos,
# melhores compradores,
# produtos em promoção*
# faturamento diário*


# from cliente import Cliente

# cliente1 = Cliente('Izabel', 12, 85296374112, 8569741235)
# cliente1.exibir()
# cliente1.cadastrar()

# from estoque import Estoque
# from estoque import Produto

# estoque = Estoque()

# pr1 = Produto("Melancia", 20, 27.99)
# pr2 = Produto("Maçã", 50, 14.98)

# estoque.add_produto(pr1)
# estoque.add_produto(pr2)

# estoque.exibir_estoque()