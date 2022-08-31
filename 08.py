#8 Programa que pergunta quanto você ganha por hora e o número de horas trabalhadas no mês. Calcula e mostra o total do seu salário no referido mês.
#programador: Eduardo Costa
#data da última atualização: 28/08/2022

ganhoPorHora = float(input('Quanto você ganha por hora?: R$ '))
horasPorMes = int(input('Número de horas trabalhadas no mês: '))
salarioTotal = ganhoPorHora * horasPorMes
print('Salário: R$ %.2f' %salarioTotal) 
