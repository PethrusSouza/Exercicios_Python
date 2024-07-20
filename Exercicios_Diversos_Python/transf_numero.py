"""Desenvolva um programa que determine o módulo de um número inteiro (se o número for negativo ele deve ser transformado em positivo).
"""
numero = int(input("Informe um numero: "))
resultado = abs (numero)
if numero < 0:
    print(f"o numero {numero} é NEGATIVO, em POSITIVO seria {resultado}.")
else:
    print(f"o numero {numero} é POSITIVO.")