nota_aluno1 = int(input("Digite a nota do aluno 1: "))
nota_aluno2 = int(input("Digite a nota do aluno 2: "))
nota_aluno3 = int(input("Digite a nota do aluno 3: "))
nota_aluno4 = int(input("Digite a nota do aluno 4: "))
nota_aluno5 = int(input("Digite a nota do aluno 5: "))

notas_totais = [nota_aluno1, nota_aluno2, nota_aluno3, nota_aluno4, nota_aluno5]

menor = min(notas_totais)
notas_totais.remove(menor)

print("--------------------------")

print(notas_totais)

print("--------------------------")