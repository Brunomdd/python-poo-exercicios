# Exercício: Salve sua classe em JSON

# Salve os dados de uma instância da sua classe em um arquivo JSON.
# Em seguida, recrie as instâncias da classe utilizando os dados salvos.
# Organize o código em arquivos separados.

import json
def salvar(dados):
    
    with open('poo.json','w',encoding='utf8') as arq:
        return json.dump(dados,arq,ensure_ascii='False',indent=2)

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def mostrar(self):
        print(f'{self.nome} - {self.idade}')

dados = {'nome':'Bruno','idade':17}
p1 = Pessoa(**dados)
salvar(dados)


