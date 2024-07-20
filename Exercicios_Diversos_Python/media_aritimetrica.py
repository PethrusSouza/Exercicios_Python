n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
media_aritmetrica = (n1 + n2 + n3) / 3
if media_aritmetrica >= 7:
    print(f"PARABÉNS, sua média foi {media_aritmetrica} e você foi APROVADO!")
else:
    print(f"A sua média foi {media_aritmetrica} e você foi REPROVADO!")
