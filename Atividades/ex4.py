lista1 = [1,2,3,4]
lista2 = [10,20,30,40,50,60]

lista_intercalada = [None] * (len(lista1) + len(lista2))

lista_intercalada[::2] = lista1
lista_intercalada[1::2] = lista2

print(lista_intercalada)
