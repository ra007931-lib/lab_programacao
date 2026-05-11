import random

lancamentos = []
total_lancamentos = 50

for _ in range(total_lancamentos):
    resultado = random.randint(1, 6) 
    lancamentos.append(resultado)

contagem_face_6 = lancamentos.count(6)

percentual = (contagem_face_6 / total_lancamentos) * 100

print(f"A face 6 apareceu {contagem_face_6} vezes.")
print(f"Percentual de ocorrências: {percentual}%")