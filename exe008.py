'''
Escreva um programa que leia o valor em metros e
o exiba em centímetros e mimímetros
'''

medida =float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000

print ('A medida {}m corresponde a {}cm e {}mm'.format(medida,cm,mm))


