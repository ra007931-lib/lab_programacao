import random 

lancamentos = []
for i in range(100):
    resultado = random.randint(1,6)
    lancamentos.append(resultado)
    
frequencia = []
for face in range(1,7):
    quantidade = lancamentos.count(face)
    frequencia.append(quantidade)
    
    print("Vetor de lançamentos (100veses)")
    print(lancamentos)
    print("\nVetor de frequências (Quantidades de vezes das face: 1, 2, 3, 4, 5, 6)")
    print(frequencia)