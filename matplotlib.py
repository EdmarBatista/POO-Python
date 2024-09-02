import matplotlib.pyplot as plt

# Dados para o gráfico
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 10, 5]

# Criando um gráfico de linha
plt.plot(x, y)

# Adicionando título e rótulos aos eixos
plt.title("Exemplo de Gráfico de Linha")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Exibindo o gráfico
plt.show()


import matplotlib.pyplot as plt

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

# Criando um gráfico de dispersão
plt.scatter(x, y, color='blue', marker='o')

plt.title("Gráfico de Dispersão")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()


import matplotlib.pyplot as plt

# Dados
categorias = ['A', 'B', 'C', 'D']
valores = [5, 7, 3, 8]

# Criando um gráfico de barras
plt.bar(categorias, valores, color='green')

plt.title("Gráfico de Barras")
plt.xlabel("Categorias")
plt.ylabel("Valores")
plt.show()


import matplotlib.pyplot as plt

# Dados
labels = ['A', 'B', 'C', 'D']
sizes = [40, 35, 15, 10]

# Criando um gráfico de pizza
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.title("Gráfico de Pizza")
plt.show()


import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

# Personalizando cor, estilo da linha e marcadores
plt.plot(x, y, color='purple', linestyle='--', marker='o')

plt.title("Gráfico com Personalização")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()


import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [0, 1, 8, 27, 64]

# Criando múltiplas linhas com legenda
plt.plot(x, y1, label='Quadrado', color='blue')
plt.plot(x, y2, label='Cubo', color='red')

plt.title("Gráfico com Legendas")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.legend()  # Adiciona a legenda ao gráfico
plt.show()

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

# Definindo o tamanho da figura
plt.figure(figsize=(8, 6), dpi=100)
plt.plot(x, y)

plt.title("Gráfico Redimensionado")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()


import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [0, 1, 8, 27, 64]

# Criando subplots
plt.figure(figsize=(10, 4))

# Subplot 1 (1 linha, 2 colunas, posição 1)
plt.subplot(1, 2, 1)
plt.plot(x, y1, color='blue')
plt.title("Gráfico Quadrado")

# Subplot 2 (1 linha, 2 colunas, posição 2)
plt.subplot(1, 2, 2)
plt.plot(x, y2, color='red')
plt.title("Gráfico Cubo")

plt.tight_layout()  # Ajusta o layout para evitar sobreposição
plt.show()




import matplotlib.pyplot as plt
import numpy as np

# Gerando dados aleatórios
dados = np.random.normal(0, 1, 1000)

# Criando um histograma
plt.hist(dados, bins=30, color='gray', alpha=0.7)

plt.title("Histograma de Dados Aleatórios")
plt.xlabel("Valor")
plt.ylabel("Frequência")
plt.show()


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dados
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Criando gráfico de superfície
ax.plot_surface(x, y, z, cmap='viridis')

plt.title("Gráfico de Superfície 3D")
plt.show()


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 10, 5]

plt.plot(x, y)
plt.title("Gráfico de Linha")

# Salvando o gráfico como PNG
plt.savefig("grafico_linha.png")
plt.show()



import matplotlib.pyplot as plt

print(plt.style.available)



import matplotlib.pyplot as plt

# Dados para o gráfico
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 10, 5]

# Lista de estilos para demonstrar
estilos = ['ggplot', 'seaborn', 'fivethirtyeight', 'bmh', 'dark_background']

for estilo in estilos:
    plt.style.use(estilo)  # Aplicando o estilo
    
    # Criando o gráfico de linha com o estilo atual
    plt.plot(x, y, marker='o')
    plt.title(f"Estilo: {estilo}")
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    
    # Exibindo o gráfico
    plt.show()
