#9) Programa que pede a temperatura em graus Fahrenheit, transforma e mostra a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
#programador: Eduardo Costa
#data da última atualização: 28/08/2022

tempF = float(input('Temperatura em graus Fahrenheit: '))
tempC = 5 * ((tempF - 32)/9)
print('Temperatura em graus Celsius: %.2f' %tempC)
