'''
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2m quadrados.
'''

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura*altura
tinta = area/2
print ('A parede tem {}m X {}m com uma área total de {:.2f}m2 '. format(largura,altura,area))
print ('Você precisará de {:.2f} litros para pintar a parede' .format(tinta))
