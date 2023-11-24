import os
from dotenv import load_dotenv

class ClienteProduto:
    def __init__(self, cpf_cliente, nome_produto, preco_produto, tipo_produto, quantidade_venda):
        self.cpf_cliente = cpf_cliente
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto
        self.tipo_produto = tipo_produto
        self.quantidade_venda = quantidade_venda
    
    def exibir(self):
        print(f"\nCPF do Cliente: {self.cpf_cliente}\nNome do Produto: {self.nome_produto}\nPreço: {self.preco_produto}\tTipo: {self.tipo_produto}\n\t\tQuantidade da venda: {self.quantidade_venda}\n\n")
    
    def venda(self):
        c = open(os.getenv("ClienteProduto"), "a")
        c.write("\n"+self.cpf_cliente+","+self.nome_produto+","+str(self.preco_produto)+","+self.tipo_produto+","+str(self.quantidade_venda))
        c.close()