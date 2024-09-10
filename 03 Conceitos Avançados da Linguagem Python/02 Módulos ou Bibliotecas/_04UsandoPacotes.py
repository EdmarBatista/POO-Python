"""
Para criar um pacote em Python, basta criar um diretório com um nome descritivo e incluir um arquivo “__init__.py”

"""

""" 
Note que, no exemplo, importamos a classe “Produto” do pacote "_04Pacote", usando
a sintaxe “from meu_pacote import Produto”. Isso significa que o arquivo “__init__.py” é
executado quando importamos o pacote, o que importa a classe “Produto” do arquivo
“produto.py”. É assim que podemos usar a classe “Produto” no programa principal.

 """

from _04Pacote import Produto


produto1 = Produto(1, "Caneta", 10)
produto2 = Produto(2, "Lápis", 5)
produto1.mostrar_detalhes()
produto1.adicionar_estoque(5)
produto1.mostrar_detalhes()
produto2.mostrar_detalhes()
produto2.adicionar_estoque(3)
produto2.mostrar_detalhes()


produtos = []
while True:
    print("\nSeLecione uma opção:")
    print("1 - Adicionar produto")
    print("2 - Atualizar produto")
    print("3 - Mostrar todos os produtos")
    print("4 - Sair")
    opcao = int(input("Opção: "))
    if opcao == 1:
        codigo = int(input("código do produto: "))
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade do produto: "))
        produto = Produto(codigo, nome, quantidade)
        produtos.append(produto)
        print("Produto adicionado com sucesso.")

    elif opcao == 2:
        codigo = int(
            input("Digite o código do produto que deseja atualizar: "))
        for produto in produtos:
            if produto.codigo == codigo:
                print("Digite as novas informações do produto:")
                nome = input("Nome: ")
                quantidade = int(input("Quantidade: "))
                produto.nome = nome
                produto.quantidade = quantidade
                print("Produto atualizado com sucesso.")
                break
            else:
                print("Produto não encontrado.")
    elif opcao == 3:
        for produto in produtos:
            produto.mostrar_detalhes()

    elif opcao == 4:
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida. Tente novamerte.")
