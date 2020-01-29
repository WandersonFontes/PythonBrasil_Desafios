#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import os
try:
	print('Iremos caucular a área do circulo apartir do raio que será informado!')
	print('+'*69)
	a = float(input('Por gentileza insira o número do raio: '))
	pi = float(3.14)
	print(f'\nA área desse circulo tem {(a**2)*pi}')
except Exception as erro:
	print('\nApresentou o senguinte erro: ',erro)
os.system('\npause')