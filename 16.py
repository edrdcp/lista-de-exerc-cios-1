#16
#programador: Eduardo Costa
#data da última atualização: 28/08/2022

areaPintar = float(input('Forneça a área a ser pintada em m²: '))
quantLitros = areaPintar / 3
quantLatas = quantLitros / 18
preco = quantLatas * 80

print('Quantidade de latas a serem compradas: ', quantLatas)
print('Preço total: R$ %.2f', preco)
