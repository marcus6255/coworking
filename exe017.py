'''
Faça um programa que leia o comprimento do cateto oposto e a
do cateto adjacente de um triângulo retângulo, calcule e mostre o
comprimento da hipotenusa.
'''

'''
co = float(input('Qual o número do cateto oposto: '))
ca = float(input('Qual o cateto adjacente: '))
hip = (co**2 + ca**2) ** (1/2)

print ('A hipotenusa vale {:.2f} '.format(hip))
'''
import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hip = math.hypot(co,ca)

print ('A hipotenusa vale {:.2f}' .format(hip))
