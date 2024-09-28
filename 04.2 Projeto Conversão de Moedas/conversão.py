import requests


def get_contacao(destino):
    #  https://api.exchangerate-api.com/v4/latest/BRL
    url = 'https://api.exchangerate-api.com/v4/latest/' + destino

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data['rates']
    else:
        print("Erro ao obter cotaçõe: ", response.status_code)
        return None


def converterCotacao(origem='USD', destino='BRL', valor=1):
    rates = get_contacao(destino)
    return round(valor / rates[origem], 2)


print(converterCotacao('USD', 'BRL'))  # contação
print(converterCotacao())  # o padrão é de dolar para real
print("100 dolares equivalem a", converterCotacao('USD', 'BRL', 100), "Reais")


def menu():
    print()
    print('1 - Converter Dólar em real')
    print('2 - Converter Euro em real')
    print('3 - Converter Libras em real')
    print('4 - Outra cotação')
    print('0 - Sair')


opcao = 1

while opcao != 0:
    menu()
    opcao = int(input('Escolha uma opção: '))
    destino = 'BRL'

    match opcao:
        case 1: origem = 'USD'
        case 2: origem = 'EUR'
        case 3: origem = 'GBP'
        case 4:
            origem=input('Digite a Origem: ')
            destino=input('Digite o Destino: ')

    if opcao:
        print()
        print('****************************************************')
        print(f'{origem} para {destino}: ', converterCotacao(origem, destino))
        print('****************************************************')
        print()
