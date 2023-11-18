from cliente import Cliente

cliente1 = Cliente('Izabel', 12, 85296374112, 8569741235)
cliente1.exibir()
cliente1.cadastrar()


from estoque import Produto

produto1 = Produto('Manga', 12, 4.50)
produto1.cadastrar_produto()
produto1.exibir_produto()
