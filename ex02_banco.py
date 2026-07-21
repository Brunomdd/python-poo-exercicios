#Exercício: Conta Bancária (POO)
#Crie uma classe chamada ContaBancaria com os atributos titular e saldo.
#Implemente os seguintes métodos:
#depositar(valor): realiza um depósito apenas se o valor for maior que zero.
#sacar(valor): realiza um saque apenas se o valor for válido e houver saldo suficiente.
#mostrar(): exibe o saldo atual da conta.
#Por fim, crie um objeto da classe, realize um depósito, um saque e exiba o saldo final.

class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self,deposito):
        if deposito <=0:
            print('Erro, número inválido para depósito')
            return
        self.saldo += deposito
        print('Deposito realizado com sucesso!')
             
    def sacar(self,sacar):
        if sacar <=0:
            print('Erro digite um valor válido para a operação')
            return
        
        if sacar > self.saldo:
            print('Erro não foi possivel realizar a operação')
        else:
            self.saldo -= sacar
            print('Saque realizado com sucesso!')
        
    def mostrar(self):
        print(f'Saldo atual: {self.saldo}')
            
conta = ContaBancaria('Bruno',10000)
conta.depositar(3000)
conta.sacar(30)
conta.mostrar()
