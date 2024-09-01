import csv

carros = [["Vw", "Virtus", "2017"],
          ["Vw", "Gol", "199"],
          ["Fiat", "Pálio", "2002"]]

with open("carros.csv", "w", newline="", encoding="utf-8") as arquivo:  # newline='' impede que fique uma linha em branco
    filieCSV = csv.writer(arquivo, delimiter=";")
    filieCSV.writerow(["Marca", "Modelo", "Ano"])
    filieCSV.writerows(carros)
