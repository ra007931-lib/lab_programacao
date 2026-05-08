#1 - definicao da constante fisica (velocidade do som em m/s)
velocidade_som = 340

#entrada
#2 leia tempo - tempo em segundos
tempo = float(input("Digite o tempo entre o clarao e o trovao(em segundos)"))

#3 processamento
#distancia em metros = velocidade * tempo 
distancia_metros = velocidade_som * tempo #  2720 metros 


#convertendo para quilometros 
distanciaKm = distancia_metros / 1000

#4 saida de dados
print(f"O raio caiu a uma distancia aproximada de {distanciaKm:.2f}km")
