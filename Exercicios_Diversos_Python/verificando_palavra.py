"""Escreva um programa que verifica se uma palavra inserida pelo usuário é "Python". E imprima se é ou não.
"""
nome = str(input("Digite a palavra 'PYTHON' para ganhar o cupom: "))
if nome.upper() == "PYTHON":
    print(f"parabéns você digitou {nome.upper()} e ganhou o cupom!")
else:
    print("você não digitou a palavra correta!")
