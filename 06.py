#6 Programa que pede o raio de um círculo, calcula e mostra sua área.
#programador: Eduardo Costa
#data da última atualização: 28/08/2022

from math import pi

r = float(input('Forneça o raio do círculo: '))
a = pi * r ** 2
print('Área do círculo: %.2f' %a)
