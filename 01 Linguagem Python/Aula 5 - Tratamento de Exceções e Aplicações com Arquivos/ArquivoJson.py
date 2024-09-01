import json

pessoas = [
    {"nome": "Orion", "telefone": "(31) 95764-3748", "endereco": "ABC"},
    {"nome": "Patrick", "telefone": "(31) 94325-3438", "endereco": "EFG"},
    {"nome": "Bob Esponja", "telefone": "(31) 94244-7523", "endereco": "HIJ"},
]

with open("pessoas.json", "w") as arquivo:
    json.dump(
        pessoas, arquivo, indent=4
    )  # joga a variável pessoas par dentro do meu arquivo , indent faz com que a indentação fique melhor, se não colocar vai ficar tudo em uma linha só
