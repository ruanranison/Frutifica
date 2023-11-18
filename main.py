import os
from dotenv import load_dotenv
from cliente import Cliente

load_dotenv()
Cliente.cadastrar()
class Main():
    def main():
        print("\n\n\t\tFRUTIFICA\n\n")
        login = input("Login: ")
        senha = input("Senha: ")

        if(login == os.getenv("ADMIN") and senha == os.getenv("SENHA")):
            print("Usuário logado!\n\n\n")
            print("\t\tCategorias\n")
            opcao = int(input("1 - Estoque\t\t\t2 - Cliente\n3 - Caixa\t\t\t4 - Relatórios\n\t\t\t5 - Sair"))
            while opcao != 5:
                if opcao == 1:
                    # menu estoque
                    break
                elif opcao == 2:
                    # menu cliente
                    break
                elif opcao == 3:
                    # menu caixa
                    break
                elif opcao == 4:
                    # menu relatorios
                    break
        else:
            print("Usuário e/ou senha incorreta!")
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