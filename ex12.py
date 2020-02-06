#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

import os 
print('Vamos fazer o calculo ideal para seu peso comparando com sua altura!\n')
alt = float(input('Por gentileza digite aqui sua altura: '))
pirnt(f'\nSeu peso ideal seria {((72.7*alt)-58):.2f} quilos.')
os.system('pause')