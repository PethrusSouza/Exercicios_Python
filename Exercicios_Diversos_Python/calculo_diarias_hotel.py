"""Um hotel cobra R$ 50,00 por diária acrescida de uma taxa de serviços. A taxa de serviços é de:
R$ 4,00 por diária, se o número de diárias for menor que 5;
R$ 3,60 por diária, caso contrário. De posse destas informações, construa um programa que solicite o número de diárias
e informe o quanto deverá ser pago pelo hóspede. """

diaria = 50
tx_serv1 = 4
tx_serv2 = 3.6
quat_diaria = int(input("Informe a qauntidade de diária: "))
if quat_diaria < 5:
    total = (diaria + tx_serv1) * quat_diaria
    print(f"Você parará R${total:.2f} por {quat_diaria} diária")
    print("*TAXA DE SERVIÇO INCLUSA.")
elif quat_diaria >= 5:
    total = (diaria + tx_serv2) * quat_diaria
    print(f"Você parará R${total:.2f} por {quat_diaria} diária")
    print("*TAXA DE SERVIÇO INCLUSA.")
    