#leia valor_produto
valor_produto = float(input("Digite valor_produto:"))
#leia desconto
desconto = valor_produto*0.15
#leia preco_final
preco_final = valor_produto - desconto
#leia print
print("Desconto: R$", desconto)
print("Total a pagar: R$", preco_final)