""" 
try: 
    n1= int(input("Número 1: "))
    n2= int(input("Número 2: "))

    resultado = n1/n2
    print(f"O resutltado da divisão é {resultado}")
except Exception as erro:   # Exception é a forma geral de capturar uma exceção, mas posso pegar erros específicos
    print(f"Ocorreu um erro -> {erro}")
     """
    
print("Entre divisão por zero ou uma string para testa os erros")
try: 
    n1= int(input("Número 1: "))
    n2= int(input("Número 2: "))

    resultado = n1/n2
    print(f"\nO resutltado da divisão é {resultado}")
except ValueError:   # Erro ao digitar uma string em vez de um número
    print("\nFavor digitar somente números")
except ZeroDivisionError:   # Erro ao digitar uma string em vez de um número
    print("\nNão é possível dividir o número por zero")
except Exception as erro:
    print("\nOcorreu um erro -> ", erro) # Exception é a forma geral de capturar uma exceção, mas posso pegar erros específicos
else:
    print("\nO programa foi executado corretamente") # Se não aconteu nenhum erro vai executar esse comando
finally:
    print("\nFim") # Executa independente se deu erro ou sucesso
    
input("\nPressione Enter para continuar...")
