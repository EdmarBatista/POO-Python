import json


class AbstractCrud:

    def detalhar(self):
        return self.__dict__
    
    def consultar(self): # Abre o arquivo
        try:
            with open('db/categorias.json') as file:
                return json.load(file)
        except Exception:
            return []  # Tenta abrir o arquivo, se der erro vai me retornar uma lista vazia

    def inserir(self):
        lista= self.consultar()

        lista.append(self.detalhar())

        with open('db/categorias.json', 'w') as file:  # Escreve sobrescrevendo o arquivo
            json.dump(lista, file, indent=4)

        print('Registro cadastrado com sucesso')

    def listarTodos(self):
        lista= self.consultar()
            
        for i,p in enumerate(lista):
            print(f"{i} - {p}")
