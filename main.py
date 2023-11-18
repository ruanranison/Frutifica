EstoqueProduto="db/EstoqueProduto.txt"
Cliente="db/Cliente.txt"
Caixa="db/Caixa.txt"
ClienteProduto="db/ClienteProduto.txt"
admin = open("db/admin.txt", 'r')
admin = admin.readlines()
LOGIN = admin[0].replace("\n", "")
PASSWORD = admin[1].replace("\n", "")

def main():
    print("\n\n\t\tFRUTIFICA\n\n")
    login = input("Login: ")
    senha = input("Senha: ")

    if(login == LOGIN and senha == PASSWORD):
        print("Usuário logado!\n\n\n")
        print("\t\tCategorias\n")
        int(input("1 - Estoque\t\t\t2 - Cliente\n3 - Caixa\t\t\t4 - Relatórios"))
    else:
        print("Usuário e/ou senha incorreta!")
        main()

main()



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


