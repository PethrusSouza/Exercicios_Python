"""Escreva um programa que encontra o maior de três números."""

n1 = float(input("Digite o PRIMEIRO número: "))
n2 = float(input("Digite o SEGUNDO número: "))
n3 = float(input("Digite o TERCEIRO número: "))
if n1 > n2 and n1 > n3:
    print(f"O PRIMEIRO número é o MAIOR.")
elif n2 > n1 and n2> n3:
    print(f"O SE|GUNDO númeor é o maior.")
elif n3 > n1 and n3 > n2:
    print(f"O TERCEIRO número é o maior.")
else:
    print("Os numeros são iguais.")