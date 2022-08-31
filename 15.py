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

print('Salário Bruto: R$ %.2f' %salarioBruto)
print('IR: R$ %.2f' %ir)
print('INSS: R$ %.2f' %inss)
print('Sindicato: R$ %.2f' %sindicato)
print('Salário Líquido: R$ %.2f' %salarioLiquido)
