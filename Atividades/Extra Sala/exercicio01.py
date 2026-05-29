while True:
    num = int(input("Digite um número (0 - para sair): "))
    if num == 0:
        print("Encerrando...")
        break
    print("----------------")
    if num >=10 and num <=50:
        print("Dado válido!")
        print("----------------")
    else: 
        print("Dado inválido!")
        print("----------------")
        