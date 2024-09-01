n1 = 10
n2 = 4
n3 = 6
n4 = 10

soma = n1 + n2 + n3 + n4

media = soma/4

# O espaçamento faz com que o que estiver espaçado esteja dentro do if
if media >=7:
    print("Aprovado")
    print("Esse print está dentro do if")
    
    
    
# Estrutura de seleção composta
# Estrutura de seleção encadinhadas
print("A média é: ", media)
if media>=7:
    print("Aprovado")
elif media<5:
    print("Reprovado")
else:
    print("Em Recuperação")
    
    
'''
Os comentários de blocos são feitos usando 3 aspas encadeadas



 ---------------------------------------
 Match

 Usando if
 
'''
# dia = int(input("Digite o número do dia da semana:"))
dia = 4


if dia ==1:
    print("Domingo")
elif dia ==2:
    print("Segunda")
elif dia ==3:
    print("Terça")
elif dia ==4:
    print("Quarta")
elif dia ==5:
    print("Quinta")
elif dia ==6:
    print("Sexta")
elif dia ==7:
    print("Sábado")
else:
    print("Esse dia não existe")
    
    
# Usando match

dia = 8
match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case other:
        print("Esse dia não existe")