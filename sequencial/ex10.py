#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
import os
f = float(input('Digite quantos graus Farenheit para realizarmos a conversão: \n'))
print(f'A conversão de {f}°F resulta em {int(((f-32)*5)/9)}°C!')
os.system('pause')