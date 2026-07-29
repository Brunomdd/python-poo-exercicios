# Crie uma classe chamada Cachorro
#class Cachorro:

    # Crie o construtor (__init__)
    # Ele deve receber:
    # - nome
    # - racao

    # Crie um método de classe chamado saudar
    # Ele deve receber uma mensagem
    # E imprimir essa mensagem

    # Crie um método de classe chamado cachorro_sem_nome
    # Ele deve receber apenas a racao
    # E retornar um objeto da classe com:
    # nome = "Anônimo"
    # racao = a informada


# Crie um cachorro chamado "Rex"
# A ração dele deve ser "Ração Premium"


# Mostre o nome e a ração do cachorro


# Chame o método saudar
# Passe a mensagem:
# "Meu cachorro favorito"


# Crie um cachorro sem nome
# Passe a ração "Carne"


# Mostre o nome e a ração do cachorro sem nome



class Cachorro:
    def __init__(self,nome,ração):
        self.nome = nome
        self.ração = ração
    @classmethod

    def cachorro_nome(cLs,nome,ração):
        return cLs(nome,ração)

    @classmethod
    def saudar(Cls,nome):
        print(nome)
    @classmethod
    def cachorro_sem_nome(cLs,ração):
        return cLs('Anônimo',ração)
        

dog = Cachorro.cachorro_nome('Rex','Premium')
print(dog.nome,dog.ração)
saudar = Cachorro.saudar(f'Meu cachorro favorito')
sem_nome = Cachorro.cachorro_sem_nome('Carne')
print(sem_nome.nome,sem_nome.ração)



