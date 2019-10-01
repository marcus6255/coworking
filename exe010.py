'''
Crie um programa que leia quanto dinheiro você tem na carteira e
mostre quantos dólares você pode comprar.
Considere US$ 1 = R$ 3,93
'''

real = float(input('Quantos reais você tem na carteira?: R$ '))
dolar = real/3.93
print ('Com R$ {:.2f} eu compro U$ {:.2f}' .format(real,dolar))
