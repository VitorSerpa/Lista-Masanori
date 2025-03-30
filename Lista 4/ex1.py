import random

lista = []
lista.append(random.randint(1, 100))
maior = menor = lista[0]


for i in range(1, 10):
    lista.append(random.randint(1, 100))
    if(lista[i] > maior):
        maior = lista[i]
    if(lista[i] < menor):
        menor = lista[i]

print(maior, menor)
print(lista)
    