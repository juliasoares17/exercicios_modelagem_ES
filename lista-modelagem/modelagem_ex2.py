class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco
    
    @property
    def preco(self):
        return self.__preco
    

class ItemPedido:
    def __init__(self, produto: Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def subtotal(self):
        preco = self.produto.preco
        return preco * self.quantidade