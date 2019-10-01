'''
Crie um programa que leia um número Real qualquer pelo teclado e
mostre a sua porção inteira.
Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
'''

'''
import math
n = float(input('Digite um número: '))
print ('O valor digitado foi {} e a sua porção inteira é {}' .format(n,math.trunc(n)))
'''

'''
from math import trunc
numero = float(input('Digite um valor: '))
print ('O valor digitado foi {} e a sua parte inteira é {}' .format(numero, trunc(numero)))
'''

num = float(input('Digite um valor: '))
print ('O valor digitado foi {} e a sua parte inteira é {}' . format(num, int(num)))



