"""Escreva um programa que verifique se um número é par ou ímpar. E imprima
essa informação."""

numero = int(input("informe um numero para saber se ele é PAR ou IMPAR: "))
if numero % 2 == 0:
    print(f"{numero} é um número PAR")
else:
    print(f"{numero} é um número IMPAR")