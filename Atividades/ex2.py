vetor = []

for i in range(5):
    vetor.append(int(input(f"Digite o valor para a posição {i}: ")))

x = int(input("Digite o valor x para buscar: "))

posicao_encontrada = -1

for i in range(len(vetor)):
    if vetor[i] == x:
        posicao_encontrada = i
        break # Para na primeira vez que encontrar

print(f"Resultado: {posicao_encontrada}")