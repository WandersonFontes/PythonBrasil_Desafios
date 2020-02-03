#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#A) o produto do dobro do primeiro com metade do segundo .
#B) a soma do triplo do primeiro com o terceiro.
#C) o terceiro elevado ao cubo.
import os
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = float(input('Agora digite um ultimo número: '))
print(f'\nA) O dobro do é {n1*2}, e a metade do segundo número é {n2/2}.')
print(f'\nB) A soma do triplo do primeiro número que é {n1*3}, mas o terceiro resulta ={(n1*3)+n3}.')
print(f'\nC) O terceiro número ao cubo é {n3**3}.')
os.system('pause')