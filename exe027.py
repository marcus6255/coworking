'''
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
Ex: Marcelo Marcus Nogueira Martins
primeiro nome: Marcelo
último nome: Martins
'''

nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Olá! Muito prazer em te conhecer!')
print ('Primeiro Nome: {}'.format(n[0]))
print ('Último Nome: {} ' .format(n[len(n)-1]))

