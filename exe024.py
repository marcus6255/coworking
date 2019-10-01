'''
Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não com nome "SANTO".
'''

cidade = str(input('Digite a sua cidade: '))
print(cidade[:5].upper() == 'SANTO')
