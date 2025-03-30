import random

def verificarPar(number : int):
    return True if number % 2 == 0 else False

listaImpar = []
listaPar = []
listaInteira = []

for i in range(0, 19):
    num = random.randint(1, 100)
    listaInteira.append(num)

    if verificarPar(num):
        listaPar.append(num)
        continue

    listaImpar.append(num)

print(listaInteira)
print(listaImpar)
print(listaPar)
