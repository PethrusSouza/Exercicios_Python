"""Escreva um programa que verifica se um número é divisível por 5.
"""
numero = int(input("Digite um numero para saber se ele é divisivel por 5:"))
if numero % 5 == 0:
    print(f"O numero{numero} é DIVISÍVEL por 5")
else:
    print(f"O número {numero} NÃO É DIVISÍVEL por 5")
