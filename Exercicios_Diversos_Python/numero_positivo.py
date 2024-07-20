"""Escreva um programa que verifica se um número é positivo, negativo ou zero."""
numero = float(input("informe um número para saber se ele é positivo, negativo ou zero: "))
if numero > 0:
    print(f"O numero {numero} é POSITIVO!")
elif numero < 0:
    print(f"O número {numero} é NEGATIVO!")
else:
    print(f"O número {numero} é NEUTRO!")