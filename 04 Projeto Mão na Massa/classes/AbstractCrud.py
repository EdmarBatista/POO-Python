import json
import os
from abc import ABC


class AbstractCrud(ABC):

    def __init__(self):
        self._criar_diretorio()

    def _criar_diretorio(self):
        if not os.path.exists('db'):
            os.makedirs('db')
            print("Diretório 'db' criado.")
        else:
            print("Diretório 'db' já existe.")

    def detalhar(self):
        return self.__dict__

    # Use @classmethod se você precisar de um método que opere em um nível de classe e não em uma instância.
    @classmethod
    def consultar(cls, item=None):  # Abre o arquivo
        try:
            with open(cls.arquivo) as file:
                lista = json.load(file)

                if isinstance(item, int):  # verifico se o item é um inteiro.   Se eu colocar "if item:" vai funcionar, porém se eu consultar o intem 0, iria dar erro, pois seria interpretado como None
                    return lista[item]
                else:
                    return lista

                # return lista[item] if isinstance(item, int) else lista    # Eu também poderia ter usado o operador ternário
        except Exception:
            return []  # Tenta abrir o arquivo, se der erro vai me retornar uma lista vazia

    def __gravarArquivo(self, lista):  # por convenção esse método é privado
        with open(self.arquivo, 'w') as file:  # Escreve sobrescrevendo o arquivo
            json.dump(lista, file, indent=4)
        print('Operação realizada com sucesso')

    def inserir(self):
        lista = self.consultar()
        lista.append(self.detalhar())
        self.__gravarArquivo(lista)

    def alterar(self, item):
        lista = self.consultar()
        lista[item] = self.detalhar()
        self.__gravarArquivo(lista)
        
    @classmethod
    def excluir(cls, item):
        lista= cls.consultar()
        del lista[item]
        # Tenho que duplicar o código, pois se eu chamar o método __gravarArquivo(self, lista)   ele vai precisar do self
        with open(cls.arquivo, 'w') as file:  # Escreve sobrescrevendo o arquivo
            json.dump(lista, file, indent=4)
        print('Operação realizada com sucesso')

    @classmethod
    def listarTodos(cls):
        lista = cls.consultar()

        for i, p in enumerate(lista):
            print(f"{i} - {p}")
