A = int(input("Digite o vetor 1: "))
B = int(input("Digite o vetor 2: "))
C = int(input("Digite o vetor 3: "))
D = int(input("Digite o vetor 4: "))
vetores = (A, B, C, D)
print("-")

print(vetores)

media = A+B+C+D / 4

print("média:",(media))

import numpy as np

indice_mais_proximo = np.abs(vetores - media).argmin()