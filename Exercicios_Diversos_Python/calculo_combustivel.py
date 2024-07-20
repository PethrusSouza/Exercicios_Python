"""Desenvolva um programa que calcule os gastos com combustível em uma
viagem. O programa deve solicitar ao usuário a distância a ser percorrida em km,
o consumo do carro em km/litro e o preço do litro do combustível. Como
resposta o programa deverá informar qual o valor em R$ a ser gasto com
combustível na viagem."""

print ("CALCULO DE COMBUSTIVEL")
distancia = int(input("informe a distância a ser pecorrida (km): "))
consumo = float(input("Quantos km/L o carro faz? "))
preco_combustivel = float(input("Qual o preço do litro do combustível? "))
valor = distancia / consumo * preco_combustivel
print(f"Querendo pecorrer uma distancia de {distancia}km com o consumo médio de {consumo}km/L")
print(f"voce irá gastar R${valor:.2f}.")