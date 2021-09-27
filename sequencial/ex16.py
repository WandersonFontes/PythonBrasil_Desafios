#Calculo de quantidade de tinta
import os


print("\n\nTire suas dúvidas em realação a pintura da sua residência!")
m =float(input('\n\nQuantos metros² você irá pintar? '))
print('\n\n==> Obs: Lembrando que a nossa tinta contém 18l e pinta uma area de 54m²! <==')
t = m/3
print(f'\nPara essa área informanda você terá que usar {t:.1f}l de tinta.\n\n')
if t<=18:
	print('\nSendo assim você só irá usar uma lata da nossa tinta!')
else:
	print('\nVocê terá que usar mais de uma lata da nossa tinta!')


os.system('pause')