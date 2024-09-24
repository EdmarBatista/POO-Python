from classes.AbstractCrud import AbstractCrud


class Produto(AbstractCrud):
    arquivo = 'db/produtos.json'  # Atributo da Classe

    def __init__(self, codigo, nome, quantidade=0, valor=0):
        super().__init__()
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
