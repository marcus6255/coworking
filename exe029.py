'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80KM/H, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada KM acima do limite.
'''

velocidade = float(input('Digite a velocidade: '))
if velocidade > 80:
    print('MULTADO!!! Você ultrapassou os 80km/h permitido!')
    multa = (velocidade - 80)*7
    print ('O valor da multa é de R$ {:.2f}'.format(multa))
print ('Tenha um bom dia! Dirija com segurança!')
