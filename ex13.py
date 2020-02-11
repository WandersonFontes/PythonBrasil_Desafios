#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7


import os

print('Vamos calcular sua massa corporal ideal!\n\n')
a = float(input('Por gentileza me informe sua altura: \n'))
print(f'Massa corporal ideal para homens com altura de {a}m é {(((72*7)*a)-58):.1f}.')
print(f'E a massa corporal ideal para as mulheres com {a}m é {(((62*1)*a)-44.7):.1f}.')








os.system('pause')