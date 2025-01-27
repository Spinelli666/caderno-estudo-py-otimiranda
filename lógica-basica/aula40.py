while True:

    first_number = input('Enter the first number: ')
    operator = input('Enter the operator: ')
    second_number = input('Enter the second number: ')

    number_valid = None

    first_number_float = 0
    second_number_float = 0

    try:
        first_number_float = float(first_number)
        second_number_float = float(second_number)
        number_valid = True
    except:
        number_valid = None
        
    if number_valid is None:
        print('Invalid number')
        continue

    valid_operator = '+-/*'

    if operator not in valid_operator:
        print('Invalid operator')
        continue

    if len(operator) > 1:
        print('Invalid operator. Please enter only one operator (+, -, *, /).')
        continue
    
    if operator == '+':
        result = first_number_float + second_number_float
    elif operator == '-':
        result = first_number_float - second_number_float
    elif operator == '*':
        result = first_number_float * second_number_float
    elif operator == '/':
        result = first_number_float / second_number_float
    else:
        print('Invalid operator')

    print(f'The result is: {result}')



    exit = input('Do you want exit? Y/N: ').lower().startswith('y')
    
    if exit is True:
        break