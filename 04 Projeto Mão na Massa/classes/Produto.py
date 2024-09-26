from classes.AbstractCrud import AbstractCrud


class Produto(AbstractCrud):
    arquivo = 'db/produtos.json'  # Atributo da Classe

    def __init__(self, codigo, nome, quantidade=0, valor=0):
        super().__init__()
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor

    def inserir(self):  # Estou sobrescrevendo o método inserir para que não aceite inserir produtos com um código já existente
        # Consultar se já existe um porduto com o código
        lista = self.consultar()
        produtoDuplicado = filter(lambda p: p['codigo'] == self.codigo, lista)
        if len(list(produtoDuplicado)): # Se o comprimento for maior que 0
            print()
            print("Já existe um produto com esse código")
        else:
            super().inserir()
