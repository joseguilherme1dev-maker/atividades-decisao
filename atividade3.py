"""3. Faça um programa que leia as notas da primeira e segunda avaliação de 
um aluno e calcule a sua média. Se a média for maior ou igual a sete 
mostre “Aprovado!”, caso contrário mostre “Reprovado!”.
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")