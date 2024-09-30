
import matplotlib.pyplot as plt

def grafico_barra(lista_moedas, lista_valores):
    plt.bar(lista_moedas, lista_valores)
    plt.title('Conversões para Real (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('BRL')
    plt.show()


def grafico_pizza(lista_moedas, lista_valores):
    plt.pie(lista_valores, labels=lista_moedas)
    plt.title('Proporção em relação ao Real Brasileiro')
    plt.show()


def grafico_dispersao(lista_moedas, lista_valores):
    plt.scatter(lista_moedas, lista_valores)
    plt.title('Conversões para Real (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('BRL')
    plt.show()

# grafico_barra(lista_moedas, lista_valores)
# grafico_pizza(lista_moedas, lista_valores)
# grafico_dispersao(lista_moedas, lista_valores)



