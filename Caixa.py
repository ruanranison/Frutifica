import os
from decouple import config
from ClienteProduto import ClienteProduto
from cliente import Cliente

class Caixa:
    def __init__ (self, caixa):
        self.caixa = caixa

    def exibir():
        arquivo = open(config("Caixa"), "r")
        c = arquivo.readline()
        print(f"Caixa: R${c}\n\n")
        
    def adicionar(valor):
        arquivo = open(config("Caixa"), "r")
        c = float(arquivo.readline())
        c = float(valor) + c
        w = open(config("Caixa"), "w")
        w.write(str(c)) 
        arquivo.close()
        print("\nAdicionado ao caixa!")
        
    def venda():
        realized = False
        arquivo = open(config("EstoqueProduto"), "r")
        c = arquivo.readlines()
        produto_venda = input('Digite o nome do produto para a venda: ')
        for i in c:
            if(i != "\n"):
                if(produto_venda == i.split(",")[0]):
                    nome_produto, quantidade, preco, tipo, pontos = i.split(",")
                    quantidade = int(quantidade)
                    quantidade_venda = int(input('Digite a quantidade do produto para a venda: '))
                    if quantidade_venda <= quantidade:
                        listaj = []
                        arquivoj = open(config("Cliente"), "r")
                        cj = arquivoj.readlines()
                        for j in cj:
                            cliente = j.replace("\n", "")
                            listaj.append(cliente)
                        cpf_consulta = input('Digite o CPF do cliente para a consulta: ')
                        for j in listaj:
                            if(j != "\n" and j != ''):
                                if(cpf_consulta == j.split(",")[2]):
                                    print("\n\nO preço do produto é: R$"+preco+"\nO valor total da venda é: R$"+str(float(quantidade_venda)*float(preco))+"\n")
                                    opcao = int(input("1 - Confirmar\t2 - Cancelar\n"))
                                    if opcao == 1:
                                        cpf = j.split(",")[2]
                                        alterado = "\n"+nome_produto+","+str((quantidade-quantidade_venda))+","+preco+","+tipo+","+str((int(pontos)+quantidade_venda))
                                        c.append(alterado)
                                        c.remove(i)
                                        w = open(config("EstoqueProduto"), "w")
                                        w.writelines(c)
                                        cp = ClienteProduto(cpf_cliente=cpf, nome_produto=nome_produto, preco_produto=preco, tipo_produto=tipo, quantidade_venda=quantidade_venda)
                                        cp.venda()
                                        Cliente.pontuacao(cpf, float(quantidade_venda)*float(preco))
                                        Caixa.adicionar(float(quantidade_venda)*float(preco))
                                        Caixa.exibir()
                                        w.close()
                                        arquivoj.close()
                                        arquivo.close()
                                        opcao = int(input("1 - Sair\t2 - Vender novamente\n"))
                                        realized = True
                                        if opcao == 1: 
                                            break
                                        else:
                                            Caixa.venda()
                                    else:
                                        opcao = int(input("\n1 - Menu\t2 - Inserir dados novamente\n"))
                                        realized = True         
                                        if opcao == 1: 
                                            break
                                        else: 
                                            Caixa.venda()
                        if realized != True:
                            print("\nDados incorretos!")
                            opcao = int(input("1 - Menu\t2 - Inserir dados novamente\n"))
                            realized = True
                            if opcao == 1: 
                                break
                            else: 
                                Caixa.venda() 

                    else: 
                        print("\nQuantidade de estoque insuficiente!\n"+nome_produto+" possui "+str(quantidade)+" unidades no estoque.")
                        opcao = int(input("\n1 - Menu\t2 - Inserir dados novamente\n"))
                        realized = True    
                        if opcao == 1: 
                            break
                        else: 
                            Caixa.venda()
        if realized != True:
            print("\nDados incorretos!")
            opcao = int(input("1 - Sair\t2 - Inserir dados novamente\n"))
            if opcao == 1: 
                print("Saindo...\n\n")
            else:
                Caixa.venda()
        arquivo.close()