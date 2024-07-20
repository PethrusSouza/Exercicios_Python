"""Uma concessionária de motos revende uma moto acrescidos 26% referidos a
impostos, 2% referente ao seguro, 8% do lucro da revendedora e 1% da
comissão do vendedor. Sabendo-se que estas porcentagens são calculadas com
relação ao preço de fábrica (preço que a revendedora compra a moto),
desenvolva um programa que calcule o preço de venda desta moto na
concessionária."""

print("REVENDA DE MOTOS")
preco_de_compra = float(input("Informe o valor de compra da moto: "))
preco_final = preco_de_compra + (preco_de_compra * 37 / 100)
print(f"o valor de revenda da moto será de R${preco_final:.2f}")