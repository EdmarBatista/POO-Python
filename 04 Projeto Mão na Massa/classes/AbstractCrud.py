import json
import os

class AbstractCrud:
    
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
    
    @classmethod # Use @classmethod se você precisar de um método que opere em um nível de classe e não em uma instância.
    def consultar(cls): # Abre o arquivo
        try:
            with open(cls.arquivo) as file:
                return json.load(file)
        except Exception:
            return []  # Tenta abrir o arquivo, se der erro vai me retornar uma lista vazia

    def inserir(self):
        lista= self.consultar()
        lista.append(self.detalhar())

        with open(self.arquivo, 'w') as file:  # Escreve sobrescrevendo o arquivo
            json.dump(lista, file, indent=4)

        print('Registro cadastrado com sucesso')

    @classmethod
    def listarTodos(cls):
        lista= cls.consultar()
            
        for i,p in enumerate(lista):
            print(f"{i} - {p}")
