'''
Crie um programa que leia o nome de uma pessoa
e diga se ela tem SILVA no nome.
'''

nome = str(input('Digite seu nome: ')) .strip()
print ('Seu nome tem Martins? {} ' .format('MARTINS' in nome.upper()))
