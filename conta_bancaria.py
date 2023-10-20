class Conta_Corrente:
    def __init__(self, agencia, numero_conta, saldo):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    # método depositar e transferir são comuns em todas as classes.
    def transferir(self,conta, valor_transferencia):
        if self.saldo > valor_transferencia:
            conta.saldo += valor_transferencia
            self.saldo -= valor_transferencia
            print(f'O saldo da conta {conta.numero_conta} agora é de {conta.saldo}')
        else:
            print(f'Transferência não realizada, saldo insuficiente. Saldo atual: {self.saldo} ')

    def depositar(self,valor_deposito):
        self.saldo += valor_deposito
        print(f'O saldo da conta {self.numero_conta} agora é de {self.saldo}')

    def get_saldo(self):
        return print(f'O saldo da conta {self.numero_conta} agora é de {self.saldo}')

    # método sacar sem implementação na superclasse
    # Esse método é sobrescrito nas subclasses
    def sacar(self):
        pass

class Conta_Fisica(Conta_Corrente):
    def __init__(self, agencia, numero_conta, saldo, renda):
        # inicializção dos atributos herdados: super()
        super().__init__(agencia, numero_conta, saldo)
        self.renda = renda

    # sobreposição do método sacar() herdado da superclasse
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Saque autorizado. O saldo da sua conta é: {self.saldo}')
        elif self.renda >= 5000:
            if valor - self.saldo <= 800:
                self.saldo -= valor
                print(f'Saque autorizado. O saldo da sua conta é: {self.saldo}')
            else:
                print('Saque não autorizado: Valor maior que o limite permitido.')
        else:
            print('Saque não autorizado. Sua conta não possui limite extra.')


class Conta_Juridica(Conta_Corrente):
    def __init__(self, agencia, numero_conta, saldo, capital):
        super().__init__(agencia, numero_conta, saldo)
        self.capital = capital

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