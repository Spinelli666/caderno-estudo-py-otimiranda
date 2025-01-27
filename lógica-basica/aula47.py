"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

word_secret = 'python'
letter_accept = ''
number_attempts = 0

while True:

    letter_d = input('\nDigite uma letra: ')
    number_attempts += 1

    if len(letter_d) > 1:
        print('Apenas uma letra, por favor!')
        continue

    if letter_d in word_secret:
        letter_accept += letter_d

    for letter_secret in word_secret:
        if letter_secret in letter_accept:
            print(letter_secret, end='')
        else:
            print('*', end='')
    

    if letter_accept == word_secret:
        os.system('clear')
        print('\nVocê acertou!')
        print ('\nPalavra formada: ', letter_accept)
        print('\nNúmero de tentativas: ', number_attempts)
        letter_accept = ''
        number_attempts = 0
