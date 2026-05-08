#leia peso
#leia altura
peso = float(input('digite o peso: '))
altura = float(input('digite a altura: '))

imc = peso / altura **2

if imc < 18.5:
    result = 'abaixo do peso'
elif imc <= 24.9:
    result = 'saudavel'
elif imc <= 34.9:
    result = 'peso em excesso'
elif imc <= 39.9:
    result = 'obesidade grau 1'
else:
    result = 'obesidade grau 3 (morbida)'

print(f'resultado: {result}')