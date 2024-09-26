from classes.Produto import Produto
from classes.Categoria import Categoria

produto=Produto('005','Mouse',100,2000)
produto.inserir()

categoria=Categoria('Eletrônico')
print(categoria.detalhar())
categoria.inserir()

print("produto.listarTodos()")
produto.listarTodos()

print("categoria.listarTodos()")
categoria.listarTodos()

print("Produto.listarTodos()")
Produto.listarTodos() # Chama o método da classe


print("print(Produto.consultar(2))")
print(Produto.consultar(2))


itemAlterar=Produto.consultar(1)
print(itemAlterar["nome"])

produto=Produto(itemAlterar['codigo'],itemAlterar['nome'],60,4000)
print(produto.detalhar())
produto.alterar(1)


Produto.excluir(0)
