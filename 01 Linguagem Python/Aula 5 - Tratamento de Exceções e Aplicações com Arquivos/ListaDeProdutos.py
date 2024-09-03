# Inicializa a lista de produtos vazia
produtos = []

# Verifica se existe um arquivo de produtos e, se existir, carrega os dados
try:
    # Abre o arquivo 'produtos.txt' em modo de leitura ('r')
    with open("produtos.txt", "r") as arquivo:
        # Itera sobre cada linha do arquivo
        for linha in arquivo:
            # Remove espaços em branco ao redor e divide a linha em partes separadas por vírgula
            codigo, nome, quantidade = linha.strip().split(",")
            # Adiciona um dicionário com o produto na lista de produtos
            produtos.append(
                {"codigo": codigo, "nome": nome, "quantidade": int(quantidade)}
            )
except FileNotFoundError:
    # Caso o arquivo não exista, o programa ignora o erro e continua
    pass

while True:
    # Exibe o menu de opções para o usuário
    print("Escolha uma opção:")
    print("1 - Incluir produto")
    print("2 - Consultar produto")
    print("3 - Alterar produto")
    print("4 - Excluir produto")
    print("5 - Listar produtos")
    print("6 - Sair")

    # Lê a opção escolhida pelo usuário
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        # Opção de incluir um novo produto
        codigo = input("Código: ")  # Lê o código do produto
        nome = input("Nome: ")  # Lê o nome do produto
        quantidade = input("Quantidade: ")  # Lê a quantidade do produto

        # Adiciona o novo produto à lista de produtos
        # Cria um dicionário com as chaves 'codigo', 'nome' e 'quantidade'
        # e armazena os valores lidos do usuário. A quantidade é convertida para inteiro.
        produtos.append({"codigo": codigo, "nome": nome, "quantidade": int(quantidade)})

        # Abre o arquivo 'produtos.txt' em modo de escrita ('w') para salvar a lista atualizada
        with open("produtos.txt", "w") as arquivo:
            # Escreve cada produto no arquivo, separando por vírgulas
            for produto in produtos:
                arquivo.write(
                    f"{produto['codigo']},{produto['nome']},{produto['quantidade']}\n"
                )
        print("Produto incluído com sucesso!")

    elif opcao == "2":
        # Opção de consultar um produto existente
        codigo = input("Código: ")  # Lê o código do produto a ser consultado
        for produto in produtos:
            # Verifica se o código do produto corresponde ao código digitado
            if produto["codigo"] == codigo:
                # Exibe as informações do produto encontrado
                print(f"Nome: {produto['nome']}")
                print(f"Quantidade: {produto['quantidade']}")
                break
        else:
            # Se o produto não for encontrado, exibe mensagem de erro
            print("Produto não encontrado!")

    elif opcao == "3":
        # Opção de alterar um produto existente
        codigo = input("Código: ")  # Lê o código do produto a ser alterado
        for produto in produtos:
            # Verifica se o código do produto corresponde ao código digitado
            if produto["codigo"] == codigo:
                nome = input("Novo nome: ")  # Lê o novo nome do produto
                quantidade = input(
                    "Nova quantidade: "
                )  # Lê a nova quantidade do produto

                # Atualiza as informações do produto na lista
                produto["nome"] = nome
                produto["quantidade"] = int(quantidade)

                # Salva a lista de produtos atualizada no arquivo
                with open("produtos.txt", "w") as arquivo:
                    for produto in produtos:
                        arquivo.write(
                            f"{produto['codigo']},{produto['nome']},{produto['quantidade']}\n"
                        )
                print("Produto alterado com sucesso!")
                break
        else:
            # Se o produto não for encontrado, exibe mensagem de erro
            print("Produto não encontrado!")

    elif opcao == "4":
        # Opção de excluir um produto existente
        codigo = input("Código: ")  # Lê o código do produto a ser excluído
        for i, produto in enumerate(produtos):
            # Verifica se o código do produto corresponde ao código digitado
            if produto["codigo"] == codigo:
                del produtos[i]  # Remove o produto da lista pelo índice

                # Salva a lista de produtos atualizada no arquivo
                with open("produtos.txt", "w") as arquivo:
                    for produto in produtos:
                        arquivo.write(
                            f"{produto['codigo']},{produto['nome']},{produto['quantidade']}\n"
                        )
                print("Produto excluído com sucesso!")
                break
        else:
            # Se o produto não for encontrado, exibe mensagem de erro
            print("Produto não encontrado!")

    elif opcao == "5":
        # Opção de listar todos os produtos
        print("Lista de produtos:")
        for produto in produtos:
            # Exibe cada produto com seus detalhes
            print(f"Código: {produto['codigo']}")
            print(f"Nome: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']}")

    elif opcao == "6":
        # Opção para sair do programa
        break
