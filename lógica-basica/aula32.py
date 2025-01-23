"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

number_int = input('Digite um número inteiro: ')
if number_int.isdigit():
    number_int = int(number_int)
    if number_int % 2 == 0:
        print(f'O número {number_int} é par.')
    else:
        print(f'O número {number_int} é ímpar.')
else:
    print('Você não digitou um número inteiro.')

# OUTRA FORMA:

try:
    number_int = int(input('Digite um número inteiro: '))
    if number_int % 2 == 0:
        print(f'O número {number_int} é par.')
    else:
        print(f'O número {number_int} é ímpar.')
except:
    print('Você não digitou um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hour = input('Digite a hora atual: ')

try:
    hour = int(hour)
    if 0 <= hour <= 11:
        print('Bom dia!')
    elif 12 <= hour <= 17:
        print('Boa tarde!')
    elif 18 <= hour <= 23:
        print('Boa noite!')
    else:
        print('Hora inválida.')
except:
    print('Você não digitou um número inteiro.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

first_name = input('Digite seu primeiro nome: ')
if len(first_name) <= 4:
    print('Seu nome é curto.')
elif 5 <= len(first_name) <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')