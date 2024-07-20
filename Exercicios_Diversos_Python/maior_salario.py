"""Escreva um programa que peça o salário de 2 pessoas e informe qual dos dois é
o maior."""

nome = input("informe seu nome: ")
salario1 = float(input("informe o valor do seu salário: "))
nome2 = input("informe o seu nome: ")
salario2 = float(input("informe o valor do seu salário: "))
if salario1 > salario2:
    print(f"O salário de {nome} é maior que o salário de {nome2}.")
elif salario2 > salario1:
    print(f"O salário de {nome2} é maior que o salário de {nome}.")
else:
    print(f"O salário de {nome} é igual ao salário de {nome2}")
