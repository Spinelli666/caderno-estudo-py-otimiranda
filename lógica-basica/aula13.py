nome = 'Bernardo SPinelli'
altura = 1.69
peso = 63
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Bernardo Spinelli tem 1.80 de altura,
# pesa 63 quilos e seu IMC é
# 22.06