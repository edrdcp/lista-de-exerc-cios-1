#14 
#programador: Eduardo Costa
#data da última atualização: 28/08/2022

pesoPeixes = float(input('Peso de peixes: '))
excesso = pesoPeixes - 50
multa = excesso * 4

print('Peso excedido em kg: %.2f' %excesso)
print('Multa: R$ %.2f' %multa)
