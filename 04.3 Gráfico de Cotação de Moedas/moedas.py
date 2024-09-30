import requests


def get_cotacao(destino='BRL'):
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
    rates = get_cotacao(destino)
    return round(valor / rates[origem], 2)