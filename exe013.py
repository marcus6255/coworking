'''
Faça um algoritmo que leia o salário de um funcionário e
mostre seu novo salário com 15% de aumento.
'''

salario = float(input('Digite o salário atual: R$ '))
aumento = salario + (salario*15/100)
print ('O funcionário com salário de R$ {:.2f}, com um aumento de 15% passará a receber R${:.2f} ' . format(salario, aumento))
