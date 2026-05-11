vetor = []

for i in range(10):
    valor = int(input(f"Digite o {i+1}º valor: "))
    vetor.append(valor)

valores_unicos = set(vetor)
quantidade_diferentes = len(valores_unicos)

print(f"Existem {quantidade_diferentes} valores diferentes no vetor.")