"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321

c = 0
new_name = ''
while c < len(nome):
    letra = nome[c]
    new_name += f'*{letra}'
    c += 1

print(new_name)
