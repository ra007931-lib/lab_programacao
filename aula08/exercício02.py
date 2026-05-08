nivel = float(input('informe o nivel atual do reservatório (%) '))
if nivel >= 90:
    status = 'critico: risco de transbordamento'
elif nivel >=50:
    status = 'adequado: fluxo normal'
elif nivel >=20:
    status = 'ATENCAO: nivel baixo'
else:
    status = 'PERIGO: nivel minimo atigido!'

print(f'status do sistema: {status}')