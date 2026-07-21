class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self,deposito):
        if self.saldo > 0:
             self.saldo += deposito
             print('Deposito realizado com sucesso!')
             
    def sacar(self,sacar):
        if sacar <=0:
            print('Erro digite um valor válido para a operação')
            return
        
        if sacar >= self.saldo:
            print('Erro não foi possivel realizar a operação')
        else:
            self.saldo -= sacar
            print('Saque realizado com sucesso!')
        
    def mostrar(self):
        print(f'{self.saldo}')
            


conta = ContaBancaria('Bruno',100)
conta.depositar(200)
conta.sacar(30)
conta.mostrar()
