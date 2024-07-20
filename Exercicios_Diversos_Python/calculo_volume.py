"""Faça um programa que calcule o volume de água em metros cúbicos de
piscinas retangulares. Solicite do usuário os valores de comprimento, altura e
largura e retorne o volume. (Volume= comprimento * largura * altura)."""

comprimento = float(input("informe o COMPRIMENTO da área: "))
largura = float(input("informe a LARGURA do área: "))
altura = float(input("informe a ALTURA da área: "))
volume = comprimento * largura * altura
print(f"de acordo com as informações fornecidas o volume necessário para o preenchimento da área é de {volume:.2f}m³")
