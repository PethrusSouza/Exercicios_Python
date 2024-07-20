"""Escreva um programa que peça a velocidade do motorista e a velocidade máxima em uma determinada avenida, 
e calcule a multa (se houver), sabendo que são pagos:

a) 50 reais se o motorista ultrapassar em até 10km/h a velocidade permitida (ex.: velocidade máxima: 50km/h;
motorista a 60km/h ou a56km/h);
b) 100 reais, se o motorista ultrapassar de 11 a 30 km/h a velocidade permitida.
c) 200 reais, se estiver acima de 31km/h da velocidade permitida.
"""

vel_motorista = int(input("Informe a velocidade do motorista: "))
vel_permitida = int(input("Informe a velocidade permitida na via: "))
multa = vel_motorista - vel_permitida
if multa > 1 and multa < 10:
    print(f"Voce passou  em {multa}km/h acima da velocidade permitada pela via, pagará uma multa de 50 reais")
elif multa > 10 and multa < 30:
    print(f"Voce passou  em {multa}km/h acima da velocidade permitada pela via, pagará uma multa de 100 reais")
elif multa > 30:
    print(f"Voce passou  em {multa}km/h acima da velocidade permitada pela via, pagará uma multa de 200 reais")
else:
    print("Voce passou na velocidade permitida pela via.")