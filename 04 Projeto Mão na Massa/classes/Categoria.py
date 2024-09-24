from classes.AbstractCrud import AbstractCrud


class Categoria(AbstractCrud):
    arquivo = 'db/categorias.json'  # Atributo da Classe

    def __init__(self, nome):
        super().__init__()
        self.nome = nome
