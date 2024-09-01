
print ("------FOR------")   
for i in range(1, 11):
    #print ("2 x",i," =",2*i) # imprime de 1 até 10
    #print("2 X {} = {}".format(i,2*i))  # substitui as {} pelos parametros de format
    print(f"2 x {i} = {2*i}")  # Melhor forma de imprimir, colocando um f na frente e o que houver calculo dentro de {}
    
    
# Uso o for quando eu sei quantas vezes serão repetidas e uso o while se eu não sei quantas vezes serão repetidas
print ("------WHILE------")   
i=1
while i<11:
    print(f"2 x {i} = {2*i}")
    i += 1
    

continuar = True
    
while continuar:
    numero = int(input("Qual tabuada?: "))
    for i in range (1,11):
        print(f"{numero} x {i} = {numero*i}")    
    continuar = input("Deseja continuar? (s/n)")
    continuar = True if continuar == 's' else False  # Operador Ternário
    
    
    
