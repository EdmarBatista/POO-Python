from datetime import datetime


# Ou recebe a data passada como parametro ou recebe a data atual
def formatarData(data=datetime.now(), formato='%d/%m/%Y'):
    # print(data)
    # as formas de formatação estão na documentação do python
    # return datetime.strftime(data, '%d/%m/%Y')
    return datetime.strftime(data, formato)

def criarData(data, formato='%Y-%m-%d'):
    return datetime.strptime(data, formato)


data = datetime(2023, 2, 17)
print(formatarData(data))
print("Data atual:", formatarData())
print("Data com formato americano:", formatarData(datetime.now(), '%m-%d'))

# Não preciso segir a ordem dos parametros, posso indicar qual eu quero passar
print('Formato especificando o parametro:', formatarData(formato='%m'))


print("Data criada com strptime:", datetime.strptime('2023-10-07', '%Y-%m-%d'))

data2 = criarData('2023-12-12')
print("Data criada com criarData e formatada com formatarData:", formatarData(data2))
