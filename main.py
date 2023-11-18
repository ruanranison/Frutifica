from cliente import Cliente

cliente1 = Cliente('Izabel', 12, 85296374112, 8569741235)
cliente1.exibir()
cliente1.cadastrar()

from estoque import Estoque
from estoque import Produto

estoque = Estoque()

estoque.exibir_estoque()
estoque.add_produto()
