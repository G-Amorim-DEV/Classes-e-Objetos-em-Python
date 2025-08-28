# Definindo a Classe
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = float(saldo)

    # Depositar o dinheiro na conta
    def depositar(self, valor):
        self.saldo += valor
    
    #Sacar 
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def exibir_saldo(self):
        print(f"O saldo de {self.titular} é de R${self.saldo:.2f}")

    
cliente1 = ContaBancaria("João", 1000)

cliente1.depositar(500)
cliente1.sacar(300)
cliente1.exibir_saldo()


