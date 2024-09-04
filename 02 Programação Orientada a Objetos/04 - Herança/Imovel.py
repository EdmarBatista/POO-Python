# Herança transmite para os filhos todos os seus atributos e seus métodos


from abc import ABC, abstractmethod  #  Abstract Basic Classes


class Imovel:
    def __init__(self, nome, uf, valor, endereco="", area=""):
        self.nome = nome
        self.uf = uf
        self.valor = valor
        self.endereco = endereco
        self.area = area

    def detalhar(self):
        print(self.__dict__)

    def calcularImposto(self):
        return self.valor * 0.02


class ImovelResidencial(Imovel):  # Para herdar eu coloca a classe pai entre os parênteses
    def __init__(self, nome, uf, valor, endereco="", area=""):
        super().__init__(nome, uf, valor, endereco="", area="")  # O self não foi passado.   Se eu não chamar o método pai, vai sobrescrever e vou ter só os novos atributos
        self.quartos = 0
        self.piscina = False


class ImovelComercial:
    ...


class ImovelRural:
    def __init__(self, hectares="", curral="", produtiva=True):
        self.hectares = hectares
        self.curral = curral
        self.produtiva = produtiva

    def mesPlantacao(self, mes):
        match int(mes):
            case 1:
                print("Milho")
            case 2:
                print("Feijão")
            case 3:
                print("Soja")
            case other:
                print("Algodão")


class Fazenda(Imovel, ImovelRural):  # Herança Múltipla
    ...


# Classe abstrata é uma classe que não pode ser instânciada. Serve para modelo de classes filhas
class ImovelAbstrato(ABC):
    def __init__(self, nome, uf, valor, endereco="", area=""):
        self.nome = nome
        self.uf = uf
        self.valor = valor
        self.endereco = endereco
        self.area = area

    def detalhar(self):
        print(self.__dict__)

    def calcularImposto(self):
        return self.valor * 0.02

    @abstractmethod
    def aluguelSugerido(self):  # Todas as classes que herdarem de imóvel abstrato devem descrever o método abstrato aluguelSugerido (Tem um contrato)
        ...


class ImovelResidencialDaAbstrata(ImovelAbstrato):
    def __init__(self, nome, uf, valor, endereco="", area=""):
        super().__init__(nome, uf, valor, endereco="", area="")
        self.quartos = 0
        self.piscina = False

    def aluguelSugerido(self):  # Têm que definir o método abstrato
        return self.valor * 0.01


# Não consigo instancia a classe Abstrata
# casaDaAbstrata = ImovelAbstrato("Imóvel Abstrato", "DF", 500000) # TypeError: Can't instantiate abstract class ImovelAbstrato without an implementation for abstract method 'aluguelSugerido'
casaDaAbstrata = ImovelResidencialDaAbstrata("Minha casa Abstrata", "SP", 300000)
print("Aluguel sugerido pela casaDaAbstrata:", casaDaAbstrata.aluguelSugerido())


fazenda = Fazenda("Fazenda Modelo", "GO", 15000000)
fazenda.detalhar()
print(fazenda.calcularImposto())
fazenda.mesPlantacao(2)


imovel = Imovel("Solar do Cerrado", "DF", 500000)
imovel.endereco = "ABC"
imovel.detalhar()

casa = ImovelResidencial("Minha casa", "SP", 3000)  # Tenho que chamar passandos os parâmetros da classe pai
print(casa.__dict__)
