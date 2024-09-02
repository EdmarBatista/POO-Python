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

