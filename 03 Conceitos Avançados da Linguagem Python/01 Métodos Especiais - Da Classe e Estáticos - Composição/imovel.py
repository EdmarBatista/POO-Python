'''
Os métodos especiais são frequentemente chamados de métodos mágicos (ou magic methods em inglês) ou métodos dunder (abreviação de "double underscore", por causa dos dois sublinhados "__" que cercam seus nomes).

Eles permitem sobrecarregar operadores padrão (como +, >, <, etc.) ou definir comportamentos personalizados para operações comuns, como converter um objeto para string (__str__) ou criar um novo objeto (__init__).

Aqui estão alguns exemplos comuns de métodos mágicos:

    __init__: Inicializador de instância (construtor).
    __str__: Retorna uma representação em string do objeto (para uso com print() e str()).
    __repr__: Retorna uma representação "oficial" da string do objeto (usada para depuração).
    __add__: Sobrecarga do operador de adição +.
    __sub__: Sobrecarga do operador de subtração -.
    __eq__: Sobrecarga do operador de igualdade ==.
    __lt__: Sobrecarga do operador de "menor que" <.
    __gt__: Sobrecarga do operador de "maior que" >.
    __len__: Define o comportamento da função len() para o objeto.
    __getitem__: Define o comportamento de indexação (como acessar elementos em uma lista).

Eles são chamados automaticamente pelo interpretador Python quando suas operações correspondentes são realizadas em objetos da classe que os implementa.

'''


# Na composição eu uso uma classe como atributo de outra classe (Não é herança)
class Categoria:
    def __init__(self, tipo=''):
        self.tipo = tipo

    def taxaAgua(self, consumo):
        match self.tipo:
            case 'Clínica': return 1 * consumo
            case 'Restaurante': return 2 * consumo
            case 'Hotel': return 2.5 * consumo


class Imovel:
    # Esse é um atributo da classe, compartilhado por todas as instâncias. Não é específico de um objeto (Não usei o self para adicioná-lo)
    imposto = 0.2

    def __init__(self, nome, quartos, suites):
        # Método especial __init__ é o construtor da classe, chamado automaticamente na criação de um objeto.
        self.nome = nome
        self.quartos = quartos
        self.suites = suites
        # Estou Instanciando um objeto da classe Categoria (Composição)
        self.categoria = Categoria()

    def __add__(self, other):
        # Método especial __add__ sobrecarrega o operador + para definir como somar dois objetos da classe Imovel.
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf + somaOther

    def __gt__(self, other):
        # Método especial __gt__ sobrecarrega o operador > para comparar dois objetos da classe Imovel.
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf > somaOther

    def __lt__(self, other):
        # Método especial __lt__ sobrecarrega o operador < para comparar dois objetos da classe Imovel.
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf < somaOther

    def __str__(self):
        # Método especial __str__ sobrecarrega a conversão de um objeto para string,
        # definindo como o objeto será representado quando usado em uma função print() ou str().
        return str(self.__dict__)

# # ---------- Métodos e atributos da classe  ----------
    def detalhar(self):  # Para chamar esse método preciso instanciar a classe
        return self.__dict__

    def somarAposentos(self):  # Para chamar esse método preciso instanciar a classe
        return self.quartos + self.suites

    @staticmethod
    def metodoEstatico():  # não pode ter o self
        print('Chamou o método estático sem criar um objeto')

    @classmethod
    # Os métodos da classe recebem como paramentro o cls (é como o self, só que da class, e não do objerto)
    def metodoClasse(cls):
        print('Chamou o método de classe que vê o imposto: ', cls.imposto)


casarao = Imovel("Casarão", 3, 4)
print(casarao.__dict__)  # Imprime o dicionário de atributos do objeto casarao.

mansao = Imovel("Mansão", 4, 5)
print(mansao.__dict__)  # Imprime o dicionário de atributos do objeto mansao.

# Utiliza o método __add__ para somar dois objetos da classe Imovel.
soma = casarao + mansao
print(soma)

# Utiliza o método __gt__ para comparar se casarao é maior que mansao.
print(casarao > mansao)
# Utiliza o método __lt__ para comparar se casarao é menor que mansao.
print(casarao < mansao)
# Utiliza o método __str__ para obter a representação em string do objeto casarao.
print(casarao)

# ---------- Métodos e atributos da classe ----------

# Chama o método de instância para somar os aposentos do objeto casarao.
print(casarao.somarAposentos())
# Chama o método de instância para somar os aposentos do objeto mansao.
print(mansao.somarAposentos())

# Chama o método estático diretamente pela classe, sem instanciar um objeto.
Imovel.metodoEstatico()
Imovel.metodoClasse()    # Chama o método de classe diretamente pela classe.
print(Imovel.imposto)    # Acessa o atributo de classe diretamente pela classe.


# ---------- Composição ----------

categoria = Categoria("Hotel")
hotel = Imovel("Hotel do Zé", 0, 150)
hotel.categoria = categoria
# O hotel não tem taxaAgua, quem tem é a categoria (Coposição é diferente de herança)
print(hotel.categoria.taxaAgua(100))
