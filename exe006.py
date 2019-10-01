'''
Crie um algoritmo que leia um número e mostre
seu dobro, triplo e raiz quadrada
'''

n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n ** (1/2)

print ('O dobro de {} é {}' .format(n,d))
print ('O triplo de {} é {} e a raiz quadrada de {} é {}'.format(n,t,n,r))

#O erro foi na raiz quadrada que era 1/2 e não n/2
