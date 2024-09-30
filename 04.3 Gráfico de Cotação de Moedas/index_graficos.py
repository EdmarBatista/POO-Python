from moedas import get_cotacao
from graficos import *

def menu():
    print()
    print('1 - Gráfico de Barras')
    print('2 - Gráfico de Pizza')
    print('3 - Gráfico de Dispersão')
    print('0 - Sair')
    print()

cotacoes = get_cotacao()

print(cotacoes['USD'])

lista_moedas = ['USD - Dólar', 'EUR - Euro', 'GBP - Libras']
lista_valores = [1/cotacoes['USD'], 1/cotacoes['EUR'], 1/cotacoes['GBP']]

opcao = 1
while opcao != 0:
    menu()
    opcao = int(input('Escolha um tipo de gráfico: '))
    match opcao:
        case 1:
            grafico_barra(lista_moedas, lista_valores)
        case 2:
            grafico_pizza(lista_moedas, lista_valores)
        case 3:
            grafico_dispersao(lista_moedas, lista_valores)