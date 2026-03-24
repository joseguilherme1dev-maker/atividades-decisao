"""1. Faça um programa que leia um número N e imprima “F1”, “F2” ou 
“F3”, conforme a condição: 
▪“F1”, se N < 10;
▪“F2”, se N = 10;
▪“F3”, se N > 10;
"""

numero = int(input("Digite um numero: "))

if numero < 10:
    print("F1")
elif numero == 10: 
    print("F2")
elif numero > 10:
    print("F3")

