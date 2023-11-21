import os
from dotenv import load_dotenv

load_dotenv()

class Caixa:
    def __init__ (self, caixa):
        self.caixa = caixa

    def exibir(self):
        print(f"Caixa: R${self.caixa}\n\n")
        
    def adicionar(valor):
        arquivo = open(os.getenv("Caixa"), "r")
        c = float(arquivo.readline())
        c = float(valor) + c
        w = open(os.getenv("Caixa"), "w")
        w.write(str(c)) 
        arquivo.close()
        print("\nAdicionado ao caixa!")
        caixa = Caixa(caixa=str(c))
        caixa.exibir()