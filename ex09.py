#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
import os 

c = int(input('Digite quantos graus Celsius para realizarmos a conversão: \n'))
print(f'A conversão de {c}ºC resulta em {((c*9)/5)+32}ºF!')

os.system('pause')