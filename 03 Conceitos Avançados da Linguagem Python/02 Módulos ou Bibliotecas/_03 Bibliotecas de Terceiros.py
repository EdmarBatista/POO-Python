""" 
Para usar bibliotecas de terceiros eu devo instalá-las 
pip install numpy

Posso também ir no site do fabricante da biblioteca e baixar de lá

Se já estive instalada aparece:
Requirement already satisfied: numpy in c:\python312\lib\site-packages (2.1.0)



NumPy (Numerical Python) é uma biblioteca em Python voltada para a computação científica e matemática, oferecendo suporte para a criação e manipulação eficiente de arrays e matrizes multidimensionais, além de uma vasta coleção de funções matemáticas para operar com esses dados. É amplamente utilizada em ciência de dados, aprendizado de máquina, análise numérica e em qualquer área que envolva grandes quantidades de dados numéricos.
Funções mais utilizadas do NumPy:

    np.array(): Cria arrays N-dimensionais, a base para todos os cálculos em NumPy.
    np.arange(): Cria arrays com uma sequência de números, similar à função range() do Python.
    np.linspace(): Gera um número especificado de elementos equidistantes entre dois valores.
    np.zeros() e np.ones(): Cria arrays de zeros ou uns, respectivamente, de tamanho especificado.
    np.reshape(): Altera a forma de um array sem modificar seus dados.
    np.mean(), np.sum(), np.max(), np.min(): Calcula a média, soma, valor máximo e valor mínimo dos elementos de um array, respectivamente.
    np.dot(): Realiza multiplicação de matrizes (produto escalar).
    np.transpose(): Transpõe um array, trocando suas linhas e colunas.
    np.random.rand(), np.random.randn(): Gera arrays de números aleatórios a partir de distribuições uniformes ou normais (gaussianas).

Essas funções cobrem desde a criação e manipulação de dados até cálculos matemáticos e estatísticos fundamentais.


"""
import numpy as np

# Criar um array NumPy a partir de uma lista
array = np.array([1, 2, 3, 4, 5])

# Exibir o array
print("Array original:", array)

# Operação: somar 10 a cada elemento do array
array_somado = array + 10
print("Array após adicionar 10:", array_somado)

# Operação: calcular a média dos elementos do array
media = np.mean(array)
print("Média dos elementos:", media)

# Operação: multiplicar todos os elementos por 2
array_multiplicado = array * 2
print("Array após multiplicação por 2:", array_multiplicado)
