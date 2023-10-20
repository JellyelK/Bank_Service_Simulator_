# Bank_Service_Simulator_
I made this program to train my skills in Python and learn how to use OOP to create better programs. This program simulates a banking service with some user in/teractions, such as a (fake) bank account for banking operations like deposits and transfers. I hope you enjoy it.

# How the program works
1. The program offers two types of bank's accounts: Personal and Business.
2. The Personal account includes the "income" attribute, which will be consulted during withdrawal operations.
3. The default account created by the client has a standard balance of $500.
4. If a Business account client attempts to withdraw an amount exceeding their available balance, the program will access their monthly income. If it is greater than $5000, the client can withdraw up to $800 more than their available balance.
5. In the case of Business accounts, if a client tries to withdraw an amount greater than their available balance, the excess amount will be deducted from their invested capital. If the client doesn't have sufficient capital, the program will refuse the transfer.

# Como o programa funciona:
1. O programa apresenta dois tipos de conta: Fisica e Juridica
2. A conta fisica possui o atributo "renda" que irá ser consultado nas operações de saque
3. A conta padrão criada pelo cliente possui um saldo padrão de 500 reais
4. Caso o cliente da conta juridica tente realizar um saque maior que o seu saldo disponivel o programa irá acessar sua renda mensal, caso essa seja maior que 5000 reais o cliente poderá sacar até 800 reais a mais que seu saldo disponivel
5. No caso da conta Juridica caso o cliente tente sacar uma quantia maior que seu saldo disponivel o valor que passar do seu saldo será descontado em seu capital investido. Caso o mesmo não tenha capital suficiente o programa recusará a transferencia
