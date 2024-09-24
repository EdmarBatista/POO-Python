# pip install scikit-learn

'''
Vai ser criada um classe de produtos com valor, peso
E vamos pedir para a ferramenta agrupar de acordo com a lógica que ela encontrar, de forma automática

'''
from sklearn.cluster import KMeans
import numpy as np


class Produto:
    def __init__(self, nome, preco, peso):
        self.nome = nome
        self.preco = preco
        self.peso = peso


produtos = [
    Produto('Produto 1', 60.50, 0.70),
    Produto('Produto 2', 25, 0.50),
    Produto('Produto 3', 5.99, 0.20),
    Produto('Produto 4', 50, 0.78),
    Produto('Produto 5', 15.99, 0.30),
    Produto('Produto 6', 8.75, 0.15),
]

precos = [[p.preco, p.peso] for p in produtos]
print(precos)

# Criação de uma matriz numpy para poder usar vários métodos da blibioteca
matriz = np.array(precos)
print(matriz)

kmeans = KMeans(n_init='auto', n_clusters=2, random_state=0).fit(matriz)  # Quero fazer um grupo de 2 cluster
labels = kmeans.labels_
print("\n\n", labels)

# A saida foi  [0 1 1 0 1 1]   O que significa que o produto 1 é do grupo 0, o produto 2 é do grupo 1...  Ele pegou os valores maiores

for i in range(2):
    print(f'Grupo {i+1}:')
    for j in range(len(produtos)):
        if labels[j] == i:
            print(' - ', produtos[j].nome)
