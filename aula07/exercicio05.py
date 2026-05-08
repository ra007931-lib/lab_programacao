op = input("deseja somar (S) ou multiplicar (M)? ")
if (op == 'S' or op == 'M'):
    x = float(input("digite o primeiro numero: "))
    y = float(input("digite o segundo numero: "))
if (op == 'S'):
    r = x + y
    print('o resultado da soma é ', r)
elif (op == 'M'):
    r = x * y
    print('o resultado da multiplicaão é', r)
else:
    print("opção invalida!")