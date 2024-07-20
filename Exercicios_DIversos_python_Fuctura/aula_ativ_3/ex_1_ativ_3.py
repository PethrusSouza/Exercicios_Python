#Crie uma lista chamada(minha_lista) com os seguinte items: 76, 92.3, “oi”, True, 4, 76.
minha_lista = [76, 92.3, "oi", True, 4, 76]
print(minha_lista)
#a) Inserir “pera” e 76 no final da lista.
minha_lista.append("pera", 76)
print(minha_lista)
#b) Inserir o valor “gato” na posição de índice 3.
minha_lista.insert(3, "gato")
print(minha_lista)
#c) Inserir o valor 99 no início da lista.
minha_lista.insert(0, 99)
print(minha_lista)
#d) Encontrar o índice de “oi”.
indice_oi = minha_lista.index("oi")
print(indice_oi)
#e) Contar o número de ocorrências de 76 na lista.
print(minha_lista.count(76)) # adicionar o print
#f) Remover a primeira ocorrência de 76 da lista.
minha_lista.remove(76)
print(minha_lista)
#g) Remover True da lista usando pop e remove.
print(minha_lista.pop(4))
print(minha_lista.remove(True))
print(minha_lista)