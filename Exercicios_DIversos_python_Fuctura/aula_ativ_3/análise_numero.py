"""escreva umprograma que solicita ao usúario um número e analise se o númeor é divisivel por 2, por 3 e por 5."""
numero = int(input("informe um numero: "))
if numero % 2 == 0:
    print(f"o número {numero} é divisivel por 2")
elif numero % 3 ==0:
    print(f"o número {numero} é divisível por 3")
elif numero % 5 == 0:
    print(f"p número {numero} é divisível por 5")
elif numero % 2 == 0 and numero % 3 == 0:
    print(f"O número {numero} é divisivel por 2 e por 3")
elif numero % 2 == 0 and numero % 5 == 0:
    print(f"O número {numero} é divisível por 2 e por 5")
elif numero % 2 == 0 and numero % 3 == 0 and numero % 5 == 0:
    print(f"O número {numero} é divisível por 2, 3 e 5")