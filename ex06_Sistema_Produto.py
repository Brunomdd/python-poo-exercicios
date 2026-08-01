# Exercício: Crie uma classe Produto

# A classe deve receber no construtor:
# - nome do produto
# - preço do produto

# Guarde esses valores em atributos internos:
# - _nome
# - _preco

# Crie um getter chamado get_nome()
# que retorna o nome do produto

# Crie um getter chamado get_preco()
# que retorna o preço do produto

# Crie um objeto chamado p1:
# Produto("Notebook", 3500)

# Mostre o nome e o preço usando apenas os getters

# Resultado esperado:
# Notebook
# 3500

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

    def get_nome(self):
        return self.nome
    def get_preco(self):
        return self.preco

p1 = Produto('Acer nitro 5',5500)
print(p1.get_nome(),p1.get_preco())
