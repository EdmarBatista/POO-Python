# pip install pandas

import pandas as pd

cidades = [
    {'nome': 'Distrito Federal', 'uf': 'DF', 'pupulacao': 3000000},
    {'nome': 'São Paulo', 'uf': 'SP', 'pupulacao': 12121212},
    {'nome': 'Rio de Janeiro', 'uf': 'RJ', 'pupulacao': 50000},
    {'nome': 'Recife', 'uf': 'RE', 'pupulacao': 10000}
]

# Preciso criar um dataframe

dataFrame = pd.DataFrame(cidades)

print(cidades)

print("\ndataFrame ->\n",dataFrame)  # um dataFrama ganha um índice e fica como uma tabela

ordenada =dataFrame.sort_values(by='pupulacao', ascending=False)
print("\n dataFrame.sort_values(by='pupulacao', ascending=False) ->\n", ordenada)

print("\n ordenada.head(2) -> \n",ordenada.head(2)) # Pegando só os dois primeiros

print("\n ordenada.head(2)['nome'] -> \n",ordenada.head(2)['nome']) # Pegando só o nome dos dois primeiros