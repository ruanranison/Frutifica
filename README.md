<h1 align="center">
    <img src="FRUTIFICA.png" />
</h1>

<h4 align="center"> 
	A FERRAMENTA QUE TRANSFORMARÁ O SEU NEGÓCIO
</h4>


## 🍉 | Sobre o projeto

O frutifica é resultado de uma solicitação feita pelo nosso professor de Lógica de Programação para que lidemos com problemas e soluções reais.

A nossa solução, basicamente, trata de resolver um problema base de qualquer estabelecimento que não tenha acompanhado a "revolução tecnológica". Utilizamos como inspiração um Hortifruti da Zona Rural de Limoeiro de Anadia para entendermos a realidade de um negócio sem a automatização das suas interações, aqui abaixo estão alguns dos requisitos funcionais contidos no nosso projeto:
- Caixa
  	- Para controle de recebimentos
  	- Possibilita a "abertura" e "fechamento" de caixa
  	- Incuída a parte de vendar e emissão de notas
  	- Registro dos clientes em compras
- Seguimento de Clientes 
  	- Para fidelizar os clientes no estabelecimento
  	- Clientes inseridos no banco de dados da empresa
  	- Cumulação de pontos para compras realizadas
- Estoque 
  	- Possibilita o controle das mercadorias
  	- Impede que os produtos venham a perecer
  	- Impede que seja o estoque seja zerado
- Relatórios
  	- Relatórios sobre todos os setores
  	- Exemplos: Cliente mais assíduo e produto mais vendido estarão nos relatórios


Como passado, o nosso público alvo direto são os funcionários e proprietários do Hortifruti e o público alvo indireto são os clientes desse ambiente. Logo, o uso do sistema será diretamente ligados os funcionários que vão usufruitor das funcionalidades.

💻 | O projeto foi desenvolvido pelos estudantes, Ray Antoniel e Ruan Ranison.
Ambos estudantes do 2º Semestre do curso de Sistemas de Informação do IFAL - Campus Arapiraca.


## Linguagem de programação

Toda a aplicação foi desenvolvida em Python

<a>
  <img src="Python-Logo.png">
</a>


## 🧾 Aqui estão os Requisitos não-funcionais da aplicação:


- **Requisitos de Produto Final**
  	- Dentro desses requisitos, cumprimos com a **confiabilidade** e a **consistência**. Haja vista que, por ser um sistema de pequena escala, não são levadas em consideração algumas modalidades, como: latência, tempo de execução e até portabilidade. O nosso sistema funciona bem na parte de confiabilidade por assegurar as necessidades do estabelecimento e é consistente por atender as demandas.
- **Requisitos Organizacionais**
  	- O software é compatível com as máquinas do Hortiifruti e a linguagem de programação utilizada (Python) funciona muito bem para a ideia.
- **Requisitos Externos**
  	- A preservação de dados dos clientes está fixa na empresa, pois não lidaremos com a internet na aplicação e o único acesso será condicionado à chave de acesso do administrador.


## 👨‍💻 Aqui está um exemplo de funcionalidade:

```bash
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
            if(cpf_consulta == i.split(",")[2]):
                nome, idade, cpf, numero_telefone, pontos = i.split(",")
                cliente = Cliente(nome=nome, idade=idade, cpf=cpf, numero_telefone=numero_telefone, pontos=pontos)
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
        arquivo = open(config("Cliente"), "r")
        cpf_consulta = input('Digite o CPF do cliente para deletar: ')
        c = arquivo.readlines()
        for i in c:
            if(cpf_consulta == i.split(",")[2]):
                c.remove(i)
                w = open(config("Cliente"), "w")
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
        arquivo = open(config("Cliente"), "r")
        cpf_consulta = input('Digite o CPF do cliente para alterar: ')
        c = arquivo.readlines()
        for i in c:
            if(cpf_consulta == i.split(",")[2]):
                nome = input('Digite o nome do cliente: ')
                idade = int(input('Digite a idade do cliente: '))
                numero_telefone = input('Digite o número de telefone: ')
                pontos = i.split(",")[4]
                resposta = input(f'Os dados do cliente são (digite SIM para confirmar e NAO para reiniciar): \nNome: {nome},\nIdade: {idade},\nCPF: {cpf_consulta},\nNúmero de Telefone:  {numero_telefone} \n')
                if resposta == "SIM":
                    c.remove(i)
                    alterado = "\n"+nome+","+str(idade)+","+cpf_consulta+","+numero_telefone+","+pontos
                    c.append(alterado)
                    w = open(config("Cliente"), "w")
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
        
    def pontuacao(cpf_consulta, valor):
        valor = int(valor)
        arquivo = open(config("Cliente"), "r")
        c = arquivo.readlines()
        for i in c:
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
        melhorComprador = sorted(c, key=lambda x: x.split(",")[4], reverse=True)
        arquivo.close()
        print("\n\n\t\t\t  Melhores compradores\n")
        for index, i in enumerate(melhorComprador):
            print(str(index + 1)+"º - "+i.split(",")[0])
        print("\n\n")
```
Esta é a nossa funcionalidade de Clientes, possibilita o cadastro, a exibição, a exclusão e a alteração dos dados dos clientes na plataforma.


## 📝 Licença

Este projeto esta sobe a licença MIT.

Feito com ❤️ por Thiago Marinho 👋🏽 [Entre em contato!](https://www.linkedin.com/in/tgmarinho/)

[nodejs]: https://nodejs.org/
[typescript]: https://www.typescriptlang.org/
[expo]: https://expo.io/
[reactjs]: https://reactjs.org
[rn]: https://facebook.github.io/react-native/
[yarn]: https://yarnpkg.com/
[vscode]: https://code.visualstudio.com/
[vceditconfig]: https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig
[license]: https://opensource.org/licenses/MIT
[vceslint]: https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint
[prettier]: https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode
[rs]: https://rocketseat.com.br
