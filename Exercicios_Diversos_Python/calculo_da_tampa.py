"""No bairro do Janga-PE existe uma empresa que fabrica tonéis "cilíndricos" de aço
que são utilizados para armazenar água. Cada tonel produzido possui uma
tampa lisa feita do mesmo material do tonel. Sabendo que a empresa gasta R$
2,50 para pintar um m2 desta tampa com um tipo especial de tinta,
desenvolva um programa que solicite as medidas desta tampa e a quantidade
de tampas a serem pintadas e informe ao usuário quanto a empresa irá gastar
para pintá-las."""

diametro_da_tampa = float(input("informe a medida do DIAMETRO da tampa (m): "))
quant_tampas = int(input("informe a quantidades de tampas a ser pintadas: "))
area_da_tampa = 3.14 * (diametro_da_tampa / 2) ** 2
area_da_tampa_arred = round(area_da_tampa)
total_areas = area_da_tampa_arred * quant_tampas
valor_total = total_areas * 2.50
print(f"para pintar {quant_tampas} tampas de {diametro_da_tampa}m de diametro")
print(f"precisará de {total_areas}m2 de tinta")
print(f"e o valor total sera de R${valor_total}")
