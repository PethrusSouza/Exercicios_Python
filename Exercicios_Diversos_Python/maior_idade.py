"""Escreva um programa que verifica se uma pessoa é maior de idade (18 anos ou
mais). E imprima se ela é ou não maior de idade."""

nome = input("informe seu nome: ")
idade = int(input("informe sua idade: "))
if idade >= 18:
    print(f"Parabéns {nome}, você tem {idade} e já tem a maior idade!")
else:
    print(f"{nome}, você tem {idade} e ainda não alcancou a maior idade")