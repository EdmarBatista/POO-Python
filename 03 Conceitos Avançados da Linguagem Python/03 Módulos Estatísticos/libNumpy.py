# pip install numpy

import numpy as np
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Calculo da média manualmente
soma = 0
for n in numeros:
    soma += n
media = soma / len(numeros)
print("Média manual:", media)



# Calculo da média usando a numpy

# crio um array numpy, que já vem com várias funções
array_numeros = np.array(numeros)
media = np.mean(array_numeros)
print("Média numpy:", media)
