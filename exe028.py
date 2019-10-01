'''
Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu.
'''

from random import randint
from time import sleep
computador = randint(0,5)
print ('$'*50)
print ('TENTE ADVINHAR O NÚMERO:')
print ('$'*50)
print ('Digite um número entre 0 e 5')
jogador = int(input('Em que número eu pensei? '))
print ('PROCESSANDO...')
sleep(5)
if jogador == computador:
    print ('PARABÉNS. VC ACERTOU O NÚMERO: {}' .format(computador))
else:
    print ('ERROU. Eu pensei o número {} e vc digitou o número {}' .format(computador, jogador))

