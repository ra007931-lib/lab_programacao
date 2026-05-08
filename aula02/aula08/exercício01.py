#leia idade 
idade = int(input("digite a idade: "))

#processamento

if (idade < 5):
    categoria = 'sem categoria muito jovem'
elif (idade <= 7):
    categoria = 'infantil A'
elif (idade <= 11):
    categoria = 'infantil B'
elif (idade <= 17):
    categoria = 'juvenil'
else:
    categoria = 'adulto'

print(f'o atleta pertence a categoria: {categoria}')