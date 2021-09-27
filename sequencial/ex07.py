#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
import os
try: 
	def quadrado():
		print(">>>Vamos calcular área do quadrado!\n",'='*50)
		a = int(input('Por gentileza informe a medida da lateral do quadrado: '))
		print(f'A área do quadrado é {a}, e o dobro do mesmo é {a*2}.')
	quadrado()
except Exception as erro:
	print('Identificamos o seguinte erro: ',erro)
	quadrado()
os.system('\npause')












