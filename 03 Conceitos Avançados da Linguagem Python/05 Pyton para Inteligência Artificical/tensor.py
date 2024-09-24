# pip install tensorflow
import tensorflow as tf

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='1'  # Tira as mensagens de aviso que aparecem no tensorflow

class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria


produtos = [
    Produto('Camisete', 29.99, 'Roupas'),
    Produto('Calça Jeans', 79.99, 'Roupas'),
    Produto('Tênis', 79.99, 'Calçados'),
    Produto('Celular', 1499.99, 'Eletrônico'),
    Produto('Notebook', 3499.99, 'Eletrônico'),
    Produto('Livro', 29.99, 'Livros'),
]

nomes = tf.constant([p.nome for p in produtos])
print(nomes)
precos = tf.constant([p.preco for p in produtos])
categorias = tf.constant([p.categoria for p in produtos])


media = tf.reduce_mean(precos)
print(media)

eletronicos=tf.boolean_mask(nomes,tf.equal(categorias,'EletrÔnicos'))

print(eletronicos)