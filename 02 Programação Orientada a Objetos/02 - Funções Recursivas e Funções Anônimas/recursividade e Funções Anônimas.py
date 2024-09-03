def fatorial(n):
    if n <= 0:  # Funções recursivas devem ter um ponto de parada
        return 1
    return n * fatorial(n - 1)


print("5! =", fatorial(5))


# ----------------------------------------------------

# Funções anônimas

# são conhecidadas como funções lambda
numeros = [4, 8, 9, 3]

resultado = []
for n in numeros:
    resultado.append(n * 2)
print(numeros, resultado)

# Toda vez que eu tiver que dar um loop em um vetor posso usar a função map


def multiplicar(n1):
    return n1 * 2


resultado = map(multiplicar, numeros)
# O map me dá um objeto map
print("map:", numeros, resultado)  # saida: <map object at 0x000001FE52CEA110>
# Preciso convertê-lo em lista
print("map:", numeros, list(resultado))


# Quando a função passada para o map é pequena eu posso usar uma função anônima (lambda)
# com o lambda eu não precisei criar uma (função)
resultado = map(lambda n: n * 2, numeros)
print("map lambda:", numeros, list(resultado))


# ----------------------------------------------------

# Funções anônimas 2

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = filter(lambda n: n % 2 == 1, numeros)
print("filter lambda:", numeros, list(resultado))