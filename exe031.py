'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 centavos por Km para viagens de
até 200km e R$ 0,45 para viagens mais longas.
'''

distancia = float(input('Digite a distância da sua viagem: '))
if distancia <=200:
    valor = distancia*0.50
    print('A sua viagem custará R$ {:.2f}'.format(valor))
else:
    valor = distancia*0.45

print ('A sua viagem custará R$ {:.2f}'.format(valor))


