#17
#programador: Eduardo Costa
#data da última atualização: 28/08/2022

import math

areaPintar = float(input('Forneça a área a ser pintada em m²: '))
quantLitros = areaPintar / 6
quantLatas = quantLitros / 18
quantGaloes = quantLitros / 3.6
preco1 = math.ceil(quantLatas) * 80
preco2 = math.ceil(quantGaloes) * 25

print('Quantidade de latas: ', math.ceil(quantLatas))
print('Preço total: R$ %.2f' %preco1)
print('Quantidade de galões: ', math.ceil(quantGaloes))
print('Preço total: R$ %.2f' %preco2)

print('Considerando um menor desperdício:')
quantLitrosFolga = quantLitros * 1.1
quantLatas_mist = quantLitrosFolga // 18 #lógica de usar o divisor inteiro
quantGaloes_mist = math.ceil((quantLitrosFolga - quantLatas_mist * 18) / 2.6)
quantMistas = quantLatas_mist + quantGaloes_mist

#calcular o preço
valor_quantLatas_mist = quantLatas_mist * 80
valor_quantGaloes_mist = quantGaloes_mist * 25
preco3 = valor_quantLatas_mist + valor_quantGaloes_mist

print('Quantidade de latas: ', quantLatas_mist)
print('Preço: R$ %.2f' %valor_quantLatas_mist)
print('Quantidade de galões: ', quantGaloes_mist)
print('Preço: R$ %.2f' %valor_quantGaloes_mist)
print('Quantidade total mistas: ', quantMistas)
print('Preço total (latas e galões): R$ %.2f' %preco3)
