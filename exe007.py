'''
Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre a sua média
'''

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2:'))
media = (n1+n2)/2

print ('A média de {} com {} é igual a {}' .format(n1,n2,media))

#Erro: tem que colocar float no lugar de int
