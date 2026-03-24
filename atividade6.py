"""Faça um programa que receba a idade de um nadador e imprima 
a sua categoria seguindo as regras:

Categoria Idade
Infantil A | 5 – 7 anos
Infantil B | 8 – 10 anos
Juvenil A | 11 – 13 anos
Juvenil B | 14 – 17 anos
Sênior | Maiores de 18 anos

"""

idade = int(input("Digite sua idade: "))

if 5 <=  idade <= 7:
    print("Su categoria é Infantil A")
elif 8 <= idade <= 10:
    print("Sua categoria é Infantil B")
elif 11 <= idade <= 13:
    print("Sua categoria é Juvenil A")
elif 14 <= idade <= 17:
    print("Sua categoria é Juvenil B")
elif idade >= 18:
    print("Sua categoria é Senior")
else:
    print("Idade insuficiente")