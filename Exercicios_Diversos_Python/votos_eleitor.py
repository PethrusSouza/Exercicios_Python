"""Desenvolva um programa que solicite que um usuário informe o número de
votos brancos, nulos e válidos de uma eleição e exiba o percentual que cada
um representa em relação ao total de eleitores."""

total_votos = int(input("informe a quantidade total dos votos: "))
votos_brancos = int(input("informe a quantidade de votos BRANCOS: "))
votos_nulos = int(input("informe a quantidade de votos NULOS: "))
votos_validos = int(input("informe a quantidade de votos VÁLIDOS: "))
perc_votos_brancos = votos_brancos / total_votos * 100
perc_votos_nulos = votos_nulos / total_votos * 100
perc_votos_validos = votos_validos / total_votos * 100
print(f"A eleição teve {total_votos} votos computados onde")
print(f"{perc_votos_brancos:.2f}% foram votos brancos")
print(f"{perc_votos_nulos:.2f}% foram votos nulos")
print(f"{perc_votos_validos:.2f}% foram votos validos")
