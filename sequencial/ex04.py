#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
import os

n1 = float(input('Por gentileza insira sua NOTA I: '))
n2 = float(input('Agora informe sua NOTA II: '))
n3 = float(input('Informe sua NOTA III: '))
n4 = float(input('Por ultimo informe sua NOTA IV: '))
m = ((n1+n2+n3+n4)/4)
print(f'A sua média é: {m:.1f}')#Método para controlar as casas decimais
if m>7.0:
	print('\nVocê foi aprovado!')
else: 
	print('\nInfelizmnete tente novamnte...')











os.system('pause')