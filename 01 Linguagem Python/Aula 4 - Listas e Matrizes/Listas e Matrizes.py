numeros = [10, 20, 30, 40]
print(numeros)
print(numeros[0])

carros = ["Palio", "Gol", "Vrtus", "Ka", "Onix"]
print(carros)
print(len(carros))

carros.append("Kombi")
print("append", carros)
carros.remove("Onix")
del carros[3]
print("remove e del", carros)
carros = sorted(carros)
print("Ordenado", carros)

print("------for in-----")
for carro in carros:
    print(carro)


print()
print("------Matrizes-----")

matriz = [[2, 3, 6, 4],
          [5, 1, 4, 2],
          [3, 6, 5, 1],
          [4, 2, 1, 5]]
print(matriz[1][2])

print()
print("------Coleções-----")

# Conjuntos
# é imutável e eu não posso alterar o valor
# Não permite elementos duplicados
conjunto = set(
    [4, 7, 2, 2, 2, 3, 0, 8]
)  # A duplicação do elemento 2 é removida automaticamente
print("Conjunto:", conjunto)

# Tupla
tupla = (3, 2, 4, 6, 0)
print("Tupla:", tupla)

# Dicionários

pessoa = {"nome": "Orion", "telefone": "(31 2385-8594)", "endereco": "ABC"}
print("Dicionário:", pessoa)
print(pessoa["nome"])
pessoas = [
    {"nome": "Orion", "telefone": "(31 2385-8594)", "endereco": "ABC"},
    {"nome": "Bob", "telefone": "(31 2385-8594)", "endereco": "EGJ"},
    {"nome": "Patric", "telefone": "(31 2385-8594)", "endereco": "QAJ"},
]
print("Array de Dicionários:", pessoas)
