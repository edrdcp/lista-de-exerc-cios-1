#15 
#programador: Eduardo Costa
#data da última atualização: 28/08/2022

ganhoPorHora = float(input('Quanto você ganha por hora?: R$ '))
horasPorMes = int(input('Número de horas trabalhadas no mês: '))

salarioBruto = ganhoPorHora * horasPorMes
ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - (ir + inss + sindicato)

print('Salário Bruto: R$', salarioBruto)
print('IR (11%): R$', ir)
print('INSS (8%): R$', inss)
print('Sindicato (5%): R$', sindicato)
print('Salário Líquido: R$', salarioLiquido)
