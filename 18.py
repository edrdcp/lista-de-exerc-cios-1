#18
#programador: Eduardo Costa
#data da última atualização: 28/08/2022

tamanho = float(input('Forneça o tamanho do arquivo para download em MB: '))
velocidade = float(input('Forneça a velocidade de um link de Internet em Mbps: '))
tempoSeg = tamanho / (velocidade / 8) #transforma bit em bytes
tempoMin = tempoSeg / 60
print('Tempo aproximado de download do arquivo usando este link: ', tempoMin, 'minutos')
