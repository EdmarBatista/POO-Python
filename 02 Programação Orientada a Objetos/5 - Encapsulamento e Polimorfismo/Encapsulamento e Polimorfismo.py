# Encapsulamento é proteger atributos e métodos para serem acessados somente por outros métodos

# Polimorfismo é capacidade de uma função ou método poder ser reescrita pela classe filha sem alterar o comportamento na classe pai.
# Em Python, o polimorfismo é alcançado usando a herança e a sobrescrita de métodos.
# É importante entender que o polimorfismo não é uma solução para todos os problemas. Em alguns casos, pode ser mais eficiente escrever código separado para objetos diferentes em vez de usar o polimorfismo.

class Imovel:
    def __init__(self, nome, uf, valor, endereco="", area=""):
        self._nome = nome
        self._uf = uf
        self._valor = valor
        self._endereco = endereco
        self._area = area

    def detalhar(self):
        print(self.__dict__)

    def calcularImposto(self):
        return "Imposto imóvel 2 %: " + str(self._valor * 0.02)

    """    
    # A forma tradicional da maioria das linguagens é criar métodos get e set para os atributos
    
    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome
    """

    # Em python eu crio uma propriedade para o get e set
    # Utilizo os métodos como se fosse atributos
    # Em python convencionou-se usar um _ para atributos protegidos e dois __ para atributos privados

    # Um atributo ou método público não tem _ e pode ser acessdo diretamente em qualquer lugar
    # Um atributo protegido _ não pode ser chamado fora da classe (Não dá erro se eu acessa, mas é uma convenção)
    # UM atributo privado __ só funciona na classe em que ele está (não poderia ser chamado nas classes filhas)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def uf(self):
        return self._uf

    @uf.setter
    def nome(self, uf):
        self._uf = uf

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, area):
        self._area = area

# ---------- ImovelResidencial ----------


# Para herdar eu coloca a classe pai entre os parênteses
class ImovelResidencial(Imovel):
    def __init__(self, nome, uf, valor, endereco="", area=""):
        # O self não foi passado.   Se eu não chamar o método pai, vai sobrescrever e vou ter só os novos atributos
        super().__init__(nome, uf, valor, endereco="", area="")
        self._quartos = 0
        self._piscina = False

    # Estou sobrescrevendo o método calcularImposto  (Polimorfismo)
    def calcularImposto(self):
        return "Imposto ImovelResidencial 0.45 %: " + str(self._valor * 0.0045)

# ---------- Instanciações ----------


imovel = Imovel("Solar do Cerrado", "DF", 500000)
imovel.endereco = "ABC"
imovel.detalhar()

""" 
imovel.setNome("Imóvel setNome")
print(imovel.getNome())
"""
imovel.nome = "Imóvel setada com @property"
print(imovel.nome)  # Estou chamando o método .nome para o get

print(imovel.calcularImposto())


casa = ImovelResidencial("Minha casa", "SP", 500000)
print(casa.calcularImposto())  # Estou chamando o método calcularImposto da classe filho
