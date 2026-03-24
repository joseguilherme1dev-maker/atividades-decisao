"""Escreva um programa que, para uma conta bancária, leia o seu número, o 
saldo, o tipo de operação a ser realizada (depósito ou retirada) e o valor 
da operação. Após, determine e mostre o novo saldo."""

conta = input("Insira o numero da sua conta: ")
saldo= float(input("Digite seu saldo: "))

print("--------- \n OPERAÇÃO BANCARIA: \n 1 - DEPOSITO \n 2 - SAQUE \n ---------")

opcao = float(input(""))

if opcao == 1:
    deposito =  float(input("Insira o valor para deposito: "))
    saldo_atual = saldo + deposito
    print(f"Seu saldo atual é {saldo_atual}")
elif opcao == 2:
    saque = float(input("Insira o valor para saque:"))
    saldo_atual = saldo - saque
    print(f"Seu saldo atual é {saldo_atual}")
else:
    print("Opção invalida")