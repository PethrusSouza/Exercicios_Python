"""Você foi contratado por um banco para realizar um sistema de saque onde o
usuário deve digitar o saldo inicial e em seguida o valor a ser sacado. O
programa deve retornar o saldo final."""

saldo_inicial = float(input("Informe o saldo da sua conta: "))
valor_sacado = float(input("quanto deseja sacar? "))
saldo_final = saldo_inicial - valor_sacado
if saldo_final >= 0:
    print (f"O saque de {valor_sacado} foi REALIZADO COM SUCESSO!!!")
    print (f"Voce ainda tem {saldo_final} na sua conta!")
else:
    print(f"Saldo insuficiente, o valor de {valor_sacado} não pode ser sacado")