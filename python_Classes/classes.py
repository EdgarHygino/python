class Primeira_class:
    def __init__(self, nome, id):
        self.cliente = nome
        self.id = id
        self.saldo = 0.0

    def Cliente(self):
        return self.cliente

    def Saldo(self):
        return self.saldo
    
    def Depositar(self, valor):
        self.saldo += valor

conta1 = Primeira_class('Edgar', 1)
conta1.Depositar(200.0)

print(conta1.Saldo())
print(conta1.Cliente())


class Cadastro:
    def __init__(self, cliente, end):
        self.cliente = cliente
        self.end = end
        self.ativo = false

    def getCliente(self):
        return self.cliente

    def getEnd(self):
        return self.end
    
conta2 = Cadastro('Joao', "rua")
print(conta2.cliente())
