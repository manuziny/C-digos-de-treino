#Faça um Programa que pergunte quanto você ganha por 
# hora e o número de horas trabalhadas no mês.

qntsHoras = float(input('Digite quanto você ganha por hora: '))
qntsHorasTrabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))

salarioBruto = qntsHoras * qntsHorasTrabalhadas

impostoDeRenda = salarioBruto * (11/100)
inss = salarioBruto * (8/100)
sindicato = salarioBruto * (5/100)
descontos = impostoDeRenda + inss + sindicato

salarioLiquido = salarioBruto - descontos

print('Salario bruto: {}'.format(salarioBruto))
print('Imposto de Renda: {}'.format(impostoDeRenda))
print('INSS: {}'.format(inss))
print('Sindicato: {}'.format(sindicato))
print('Descontos: {}'.format(descontos))
print('Salario líquido: {}'.format(salarioLiquido))