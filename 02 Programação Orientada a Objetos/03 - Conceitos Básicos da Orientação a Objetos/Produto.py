# Classes em python começam com letra maiúscula
class Produto:
    #   ...  ## ... ou pass não faz nada

    # O __init__ é o construtor da classe, esse método é executado toda vez que a classe é instânciada
    # self equivale ao this de outras linguagens
    # def __init__(self)  # Se eu não colocar mais variaveis posso instâncias com Produto()
    def __init__(self, nome, valor, modelo="", quantidade=0):  # Se eu colocar variáveis elas serão obrigatórias na instânciação: Produto("NotebookBarato",100), o self não conta como parâmetro obrigatório
        # Se eu não colocar o modelo ele fica como '' por padrão
        self.nome = nome
        self.marca = "Samsung"
        self.modelo = modelo
        self.valor = valor
        self.quantidade=quantidade
        
    def vender(self, quantidade): # A rigor os métodos de uma classe precisão receber o self
        if(quantidade> self.quantidade):
            print("Não ha estoque suficiênte")
            print(f"Quntidade máxima: {self.quantidade}")
        else:   
            self.quantidade = self.quantidade - quantidade
        
    def comprar(self, quantidade):
        self.quantidade = self.quantidade + quantidade


# De uma única classe eu posso criar vários objetos
produto = Produto("NotebookBarato", 100, "Modelo",20)

produto2 = Produto("Nome do produto", 100)  # O modelo ficou no padrão = ''
produto2.nome = "Notebook"  # Estou criando a propriedade de forma dinâmica
produto2.marca = "LG"

print(produto)  # <__main__.Produto object at 0x00000280BF549DC0>
print(produto.__dict__)

print(produto2)
print(produto2.__dict__)  # Mostra os atributos de um objeto  ->  {'nome': 'Notebook', 'marca': 'LG', 'modelo': '', 'valor': 100, 'quantidade': 0}
produto2.comprar(80)
produto2.vender(20)
# tinha 0, comprei 80 e vendi 20
print(produto2.__dict__) # {'nome': 'Notebook', 'marca': 'LG', 'modelo': '', 'valor': 100, 'quantidade': 60}

# tentando vender mais do que têm
produto2.vender(100)