"""4. Faça um algoritmo/programa que receba dois números e diga se o 
primeiro é maior que o segundo, se são iguais ou se o segundo é maior 
que o primeiro."""

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 > numero2 :
    print("O primeiro numero é maior!")
elif numero1 == numero2:
    print("Os numeros são iguais!")
else:
    print("O segundo numero é maior!")
