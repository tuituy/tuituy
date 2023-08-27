from random import randint
from time import sleep
computador = randint(0,5) # pc escolhe um número
print('*-'*21)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('*-'*21)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você consegiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador,jogador))


