first_value = input('Digite um número: ')
second_value = input('Digite outro número: ')

if first_value < second_value:
    print(f'O {first_value} é menor do que o {second_value}')
elif first_value > second_value:
    print(f'O {first_value} é maior do que o {second_value}')
elif first_value == second_value:
    print('Os valores são iguais')
else:
    print('Os valores são diferentes')