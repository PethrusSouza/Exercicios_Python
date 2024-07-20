"""Escreva um programa que implemente uma calculadora básica que realiza adição, subtração, multiplicação e divisão
com base na escolha do usuário (solicita qual o número e operação)."""

print("""DIGITE UMA OPÇÃO:
[1] ADIÇÃO
[2] SUBTRAÇÃO
[3] MULTIPLICAÇÃO
[4] DIVISÃO""")
escolha = int(input("Digite o numero correspondente a operação desejada: "))
if escolha == 1:
    print ("você escolheu a tabuada de ADIÇÂO")
    numero = int(input("Digite um número para saber sua tabuada: "))
    for c in range(1, 11):
        print(f"{numero} + {c} = {numero+c}")
elif escolha == 2:
    print("você escolheu a tabuada de SUBTRAÇÃO")
    numero = int(input("Digite um número para saber sua tabuada: "))
    for c in range(1, 11):
        print(f"{numero} - {c} = {numero-c}")
elif escolha == 3:
    print("você escolheu a tabuada de MULTIPLICAÇÃO")
    numero = int(input("Digite um número para saber sua tabuada: "))
    for c in range(1, 11):
        print(f"{numero} x {c} = {numero*c}")
elif escolha == 4:
    print("você escolheu a tabuada de DIVISÃO")
    numero = int(input("Digite um número para saber sua tabuada: "))
    for c in range(1, 11):
        print(f"{numero} ÷ {c} = {numero/c:.1f}")
else:
    print("OPÇÃO INVALIDA, TENTE NOVAMENTE")



