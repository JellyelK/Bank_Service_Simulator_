#Questão 01:
class Conta_corrente:
    def __init__(self, agencia, numero_conta, saldo ):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, conta, valor_deposito):
        conta.saldo = self.saldo + valor_deposito

    def sacar(self, valor):
        pass
        
class Conta_fisica(Conta_corrente):
    def __init__(self, agencia, numero_conta, saldo, renda_mensal):
        super().__init__(agencia, numero_conta, saldo)
        self.renda_mensal = renda_mensal 
    def depositar(self):
        return super().depositar()
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque autorizado com sucesso. Saldo atual {self.saldo}"
        elif valor - self.saldo <=800 and self.renda_mensal >=5000:
            self.saldo -= valor
            return f"Saque autorizado com sucesso. Saldo atual {self.saldo}"
        else:
            return f"Saque não autorizado, saldo e limite insuficiente"

class Conta_juridica(Conta_corrente):
    def __init__(self, agencia, numero_conta, saldo, capital_investido):
        super().__init__(agencia, numero_conta, saldo)
        self.capital_investido = capital_investido
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Saque autorizado. O saldo da sua conta é: {self.saldo}.')
        elif valor - self.saldo  <= self.capital:
            self.capital -= (valor - self.saldo)
            self.saldo = 0
            print(f'O saldo da conta é {self.saldo}. '
                  f'O saldo atual do capital investido é {self.capital}.')
        else:
            print(f'Saque não autorizado. Valor do saque maior '
                  f'que o disponível (saldo + capital)')
    
