#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

import os
print('Olá vamos fazer o confitmar o valor do seu salário!\n','+'*50)
v = int(input('Você sabe informar o valor da sua hora? 1=SIM / 2=NÂO '))
if v == 2:
	print('Sem problemas, vamos caucular essas informações contigo!')
	st = float(input('Por gentileza, me informe o valor total do seu salário: '))
	h = int(input('Quantas horas você trabalha durante o mês? '))
	hr = float(f'Sua hora de trabalho vale: R${(st/h):.2f}')
	nada = input()
else:
	vt = float(input('Digite o valor da sua hora de trabalho: R$'))
	ht = int(input('Agora me informe a quantidade de horas você trabalha por mês: '))
	print(f'O valor do seu salário mensal é de R${(vt*hr):.2f}')
	nada = input()




os.system('pause')