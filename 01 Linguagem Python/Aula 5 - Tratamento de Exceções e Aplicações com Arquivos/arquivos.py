"""
Se eu uso w  vai apagar tudo para escrevere denovo 
Se eu uso a+ vai adicinar coisar no final do arquivo

"""


arquivo = open('pessoas.txt','w')  # Se o arquivo não existe ele será criado

arquivo.write("Bob Esponja\n")
arquivo.write("Orinoz\n")
arquivo.write("Maria\n")

arquivo.close() # Fecha o arquivo após seu uso

arquivo2 = open('pessoas.txt','a+')  # Se o arquivo não existe ele será criado
arquivo2.write("\n---- Adicionados com a+ ---\n\n")
arquivo2.write("Patrick\n")
arquivo2.write("Sirigueijo\n")

arquivo2.close() # Fecha o arquivo após seu uso


# Abre o arquivo dentro do bloco eu quando saio do bloco já fecha o arquivo

with open("pessoas.txt",'r+') as arquivoLeitura: # r+ somente leitura
    for linha in arquivoLeitura:
        print(linha)
# Ao sair do block já fecha o arquivo


# Arquivos Json e CSV