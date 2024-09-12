import numpy as np
import pandas as pd


class Paciente:
    def __init__(self, nome, idade, sexo, peso, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.peso = peso
        self.altura = altura


pacientes = {
    "Paciente 1": Paciente('Maria', 25, 'F', 60, 1.70),
    "Paciente 2": Paciente('Orion', 30, 'M', 80, 1.80),
    "Paciente 3": Paciente('João', 45, 'M', 70, 1.85),
    "Paciente 4": Paciente('Ana', 35, 'F', 90, 1.65)
}

# Crio uma lista com todos os dics
lista_pacientes = [p.__dict__ for p in pacientes.values()]

print("\n p.__dict__ for p in pacientes.values()]   ->\n", lista_pacientes)

# Crio um dataFrame para o pandas usando as chaves de pacientes como índice
df_pacientes = pd.DataFrame.from_records(lista_pacientes, index=pacientes.keys())
print('\n pd.DataFrame.from_records(lista_pacientes, index=pacientes.keys())   ->\n', df_pacientes)

# Adiciono o IMC
df_pacientes['IMC'] = df_pacientes.apply(lambda i: i.peso/(i.altura**2), axis=1)
print(df_pacientes)

media = np.mean(df_pacientes['IMC'])
print('Média dos IMCs:', media)

sobrepeso = df_pacientes[df_pacientes['IMC'] > 25]
print('Sobrepeso:\n', sobrepeso)

percental = len(sobrepeso)/len(df_pacientes)*100
print('Percentual de sobrepeso:', percental,"%")
