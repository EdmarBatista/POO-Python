def dividir(n1, n2):
    resultado=n1/n2
    print(f'O resultado da divisão é {resultado}')

dividir(5,80)

def dividir2(n1, n2):
    resultado=n1/n2
    return resultado

print("O resultado da divisão2 é", dividir2(80,5))


# Escopos
n1=7 # Escopo global
n3=10
def soma(n1,n2): # Esse n1 é difirente do que está no escopo global
    print(n1,n2)
    print(n3) # A função localiza n3 pois ela está no escopo global

soma(5,8)


# Exemplo prático

def somar(n1,n2):
    return n1+n2

def subtrair(n1,n2):
    return n1-n2

def multiplicar(n1,n2):
    return n1*n2


def calcular(n1,n2, operador):
    match operador:
        case '+': return somar(n1,n2)
        case '-': return subtrair(n1,n2)
        case '*': return multiplicar(n1,n2)
        case '/': return dividir(n1,n2)
        case other: return 'Operador não encontrado'
        
print(calcular(5,10,'+'))
print(calcular(5,10,'-'))
print(calcular(5,10,'a'))

# função que retorna o maior valor de uma lista
def encontrar_maior_valor(lista):
    maior = lista[0]
    for valor in lista:
        if valor > maior:
            maior = valor
    return maior

numeros = [2, 8, 4, 10, 5]
maior_numero = encontrar_maior_valor(numeros)
print("Maior número",maior_numero) # saída: 10


#  As funções em Python podem retornar múltiplos valores usando tuplas.
def calcular_quadrado_e_cubo(numero):
    quadrado = numero ** 2
    cubo = numero ** 3
    return quadrado, cubo

resultado_quadrado, resultado_cubo = calcular_quadrado_e_cubo(3)
print("resultado_quadrado",resultado_quadrado) # saída: 9
print("resultado_cubo",resultado_cubo) # saída: 27