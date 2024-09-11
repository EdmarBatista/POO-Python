# pip install matplotlib

import matplotlib.pyplot as plt

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
qtdTI = [60, 52, 76, 89, 108, 95]
qtdRH = [40, 72, 17, 28, 87, 56]


navegadores = ['Chrome', 'Firefox', 'Edge']
qtdNavegadores = [1200, 600, 200]


plt.plot(meses, qtdTI, label="TI", color='blue', linestyle='--', marker="o")
plt.plot(meses, qtdRH, label="RH", color='#ff0000')
plt.legend()
plt.title("Chamados Abertos")
plt.xlabel('Meses')
plt.ylabel('Quantidade')
plt.show()


plt.bar(meses, qtdRH)
plt.title("Chamados Abertos")
plt.xlabel('Meses')
plt.ylabel('Quantidade')
plt.show()


plt.bar(meses, qtdTI, label="TI", color='blue', linestyle='--')
plt.bar(meses, qtdRH, label="RH", color='#ff0000')
plt.legend()
plt.title("Chamados Abertos")
plt.xlabel('Meses')
plt.ylabel('Quantidade')
plt.show()


cores = ['red', 'orange', 'blue']
plt.pie(qtdNavegadores, labels=navegadores, colors=cores)
plt.show()
