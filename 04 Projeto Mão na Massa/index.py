from classes.Produto import Produto
from classes.Categoria import Categoria

produto=Produto('001','Relogio',100,2000)
produto.inserir()

categoria=Categoria('Eletrônico')
print(categoria.detalhar())
categoria.inserir()


produto.listarTodos()

