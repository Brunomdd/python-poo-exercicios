#  Recriando Classe Pessoa

import json 
from ex03_salvando_classe import Pessoa
def carregar():
    with open('poo.json','r',encoding='utf-8')as arq:
        return json.load(arq)
    
dados = carregar()

p1 = Pessoa(**dados)
print(p1.nome,p1.idade)

    
    