# Exemplo de bibliotecas padrões do python

import math  # Biblioteta padrão do python para números
import random  # Para geração de números aleatórios

nota = 6.8
print("nota:", nota)
print("round:", round(nota))

nota = 6.855
print("nota:", nota)
print("round(nota, 2)", round(nota, 2))  # Duas casas decimais

# Arredonda para baixo
print("math.floor(nota):", math.floor(nota))
# Arredonda para cima
print("math.ceil(nota):", math.ceil(nota))
print("math.pi:", math.pi)

print("\n---------- random ----------\n")

print("random.random():", random.random())
print("round(random.random()*100):", round(random.random()*100))

# Imprime números aleatórios entre 1 e 10, incluindo os extremos
print("random.randint(1, 10):", random.randint(1, 10))
