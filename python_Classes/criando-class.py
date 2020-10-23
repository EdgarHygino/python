class Conta:
    def __init__(self, nome, numero):
        self.cliente = nome
        self.num = numero
        self.saldo  = 0.0

    def Saldo(self):
        return self.saldo

    def getCliente(self):
        return self.cliente

    def Depositar(self, valor):
        self.saldo += valor

conta1 = Conta('Jão', 1)
conta1.Depositar(100.00)
print(conta1.Saldo())
print(conta1.getCliente())

conta2 = Conta('Maria', 2)
conta2.Depositar(200.00)
print(conta2.Saldo())
print(conta2.getCliente())