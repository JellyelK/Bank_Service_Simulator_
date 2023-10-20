from conta_bancaria import Conta_Fisica
from conta_bancaria import Conta_Juridica

#ALGUMAS OBSERVAÇÕES:
# 1. O programa a seguir simula um atendimento bancário, porém o mesmo vem com algumas configurações previamente setadas. Como por exemplo o saldo da conta do cliente, ja que o mesmo (Em uma situação real) não consegue configurar o saldo que terá em sua conta. Logo o saldo padrão da conta de cada usuário será de 500 reais.

#2 . Para otimizar o uso do programa ja deixei configurado duas contas para transferência ou depósito:

#3. O programa reinicia logo após a operação realizada pelo usuário e retorna ao laço inicial

#-------------------------------------------------------------------------------------------------------#

#SOME OBSERVATIONS:
# 1. The following program simulates a banking service, but it comes with some pre-set configurations. For example, the client's account balance, since they cannot configure their account balance in a real-life situation. Therefore, the default account balance for each user will be 500 Brazilian Reais.

#2. For user optimization of the program, I have pre-set some banking accounts for operations like bank transfer or bank deposit.

#3. The program reboot after the client makes some banking operations, then it starts over again

#4. Shortly i'll make a 100% english version of this program, but for now i hope you like it

#4. Enjoy the program :-)

# Conta 1 (Account_1)
conta_1 = Conta_Fisica("0075", 7788, 300, 5000 )

#Conta 2 (Account_2)
conta_2 = Conta_Fisica("0075", 8877, 300, 5000 )

#Programa
while True:
    print("O que deseja fazer?: \n--------------------\n 1. Déposito\n 2. Acessar conta")
    verificacao = int(input("> "))

    if verificacao == 1:
        print("Digite o número correspondete à conta que deseja depositar\n 0. Conta própia \n 1. Conta 1 \n 2. Conta 2")
        comando = int(input("> "))
        valor = float(input("Digite o valor que deseja depositar: "))
        if comando == 1:
            conta_1.depositar(valor)
            continue
                                
        elif comando == 2:
            conta_2.depositar(valor)
            continue
                            
        elif comando == 0:
            print("Logue-se em sua conta para realizar o depósito")
            print("----------------------------------------------")
            print("")    
            continue        
        else:
            print("Digite um número válido")   
            continue     

    elif verificacao == 2:
        while True:
            #Verifica o tipo de conta do usuário, se é fisica ou juridica
            #Check if the user's account type is "fisica" or "juridica" (physical or legal account) 
            tipo_conta = input("Digite o tipo da sua conta (fisica ou juridica): ")
            if tipo_conta == "fisica" or tipo_conta =="juridica":
                #Conta Fisica (Physical Account):
                if  tipo_conta == "fisica":
                    agencia = input("Digite o número de agencia da sua conta: ")
                    numero = input("Digite o número da conta: ")
                    renda = float(input("Digite sua renda mensal: "))
                    teste_agencia = isinstance(agencia, int)
                    teste_numero_conta = isinstance(numero, int)
                    if False:
                        print("Erro, agencia ou número de conta está faltando")
                        continue
                    else:
                        while True:
                            operacao = input("Digite a operação que deseja fazer: saque, transferência, depósito: ")
                            conta_pessoal = Conta_Fisica(agencia, numero, 500, renda)
                            if operacao == "saque":
                                valor = float(input("Digite o valor que deseja sacar: "))
                                conta_pessoal.sacar(valor)
                                break
                                
                            elif operacao == "transferencia":
                                print("Digite o número correspondete à conta que deseja transferir \n 1. Conta 1 \n 2. Conta 2")
                                comando = int(input("> "))
                                valor = float(input("Digite o valor que deseja transferir: "))
                                if comando == 1:
                                    conta_pessoal.transferir(conta_1, valor)
                                    break
                                    
                                elif comando == 2:
                                    conta_pessoal.transferir(conta_2,valor)
                                    break
                            elif operacao == "deposito":
                                valor = float(input("Digite o valor que deseja depositar: "))
                                conta_pessoal.depositar(valor)
                                break
                                
                            else:
                                print("Selecione uma operação válida")

                #Conta Juridica (Legal Account):
                elif tipo_conta == "juridica":
                    agencia = input("Digite o número de agencia da sua conta: ")
                    numero = input("Digite o número da conta: ")
                    capital = float(input("Digite seu capital investido: "))
                    teste_agencia = isinstance(agencia, int)
                    teste_numero_conta = isinstance(numero, int)
                    if False:
                        print("Erro, agencia ou número de conta está faltando")
                        continue
                    else:
                        while True:
                            operacao = input("Digite a operação que deseja fazer: saque, transferência, depósito: ")
                            conta_pessoal = Conta_Juridica(agencia, numero, 500, capital)
                            if operacao == "saque":
                                valor = float(input("Digite o valor que deseja sacar: "))
                                conta_pessoal.sacar(valor)
                                break
                                
                            elif operacao == "transferencia":
                                print("Digite o número correspondete à conta que deseja transferir \n 1. Conta 1 \n 2. Conta 2")
                                comando = int(input("> "))
                                valor = float(input("Digite o valor que deseja transferir: "))
                                if comando == 1:
                                    conta_pessoal.transferir(conta_1, valor)
                                    break
                                    
                                elif comando == 2:
                                    conta_pessoal.transferir(conta_2,valor)
                                    break
                            elif operacao == "deposito":
                                valor = float(input("Digite o valor que deseja depositar: "))
                                conta_pessoal.depositar(valor)
                                break
                                
                            else:
                                print("Selecione uma operação válida")
            else:
                print("Error")
                continue
    else: 
        print("Erro! Digite um número válido")
