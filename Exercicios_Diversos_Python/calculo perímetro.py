"""Escreva um programa que leia a largura e a altura de um retA^ngulo e calcule
seu perímetro (Saída deve ser "O perímetro é ___")."""

altura = float(input("Informe a altura do retângulo:"))
largura = float(input("Informe a largura do retângulo: "))
perimetro = 2*(altura + largura)
print(f"o perímetro do retângulo é {perimetro:.2f}")