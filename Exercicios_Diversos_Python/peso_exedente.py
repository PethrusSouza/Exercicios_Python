"""No bairro do Janga existe uma lei que toda vez que um pescador traz um peso de peixes maior que o estabelecido
pelo regulamento de pesca (50 quilos) deve pagar uma multa de R$4,00 por quilo excedente. A prefeitura precisa
que você faça um programa que solicite o peso de certa quantidade de peixes e caso haja excesso de peso, mostre
qual é este peso (em quilos) e quanto de multa deverá ser paga. Caso não haja excesso, deverá ser mostrada a mensagem
“Parabéns por não ultrapassar o limite”. """

quant_pescado = int(input("Informe a quantidade de peixe pescado(kg): "))
limite_diario = 50
multa = 4
exedente = quant_pescado - limite_diario
valor_multa = exedente * multa
if exedente > 0:
    print(f"O limite diário a ser pescado é de {limite_diario}kg, você exedeu o limite em {exedente}kg")
    print(f"e pagará uma multa de R${valor_multa:.2f}")