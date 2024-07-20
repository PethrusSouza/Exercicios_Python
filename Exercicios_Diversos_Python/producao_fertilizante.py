"""Para se produzir um determinado tipo de fertilizante, uma fábrica precisa
misturar três partes de Nitrogênio (N), duas partes de Potássio (K) e uma parte
de Fósforo (P). De posse dessa informação, desenvolva um programa que
solicite como informação uma determinada quantidade (em Kg) deste
fertilizante e informe ao usuário a quantidade (em Kg) necessária de
Nitrogênio, Potássio e Fósforo para a mistura."""

quant_fertilizante = float(input("informe quantos quilos de fertilizantes você quer produzir: "))
nitrogenio = quant_fertilizante / 6 * 3
potassio = quant_fertilizante / 6 * 2
fosforo = quant_fertilizante / 6
print(f"para produzir {quant_fertilizante}kg de fertilizantes, será necessário")
print(f"{nitrogenio:.2f}kg de nitrogênio")
print(f"{potassio:.2f}kg de potássio")
print(f"{fosforo:.2f}kg de fósforo")