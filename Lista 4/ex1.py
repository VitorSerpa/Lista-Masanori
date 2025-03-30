import random

vetor = []
vetor.append(random.randint(1, 100))
maior = menor = vetor[0]


for i in range(1, 10):
    vetor.append(random.randint(1, 100))
    if(vetor[i] > maior):
        maior = vetor[i]
    if(vetor[i] < menor):
        menor = vetor[i]

print(maior, menor)
print(vetor)
    