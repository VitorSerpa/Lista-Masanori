import random

lista1 = []
lista2 = []
listaIntercalada = []

for i in range(0, 10):
    lista1.append(random.randint(1, 100))
    lista2.append(random.randint(1, 100))
    listaIntercalada.append(lista1[i])
    listaIntercalada.append(lista2[i])

print(lista1)
print(lista2)
print(listaIntercalada)

    