#João Papo de Pescador
import os
print('\nCalculo de multas para peso superior á 50kl de peixes!\n')
q = float(input('Por gentileza digite quantos quilos de peixes foi pesado:\n\n'))
print('\n\n==> Sabendo que cada quilo além do limite é pago o valor de R$4,00. <==\n\n')
e = q-50
m = e*4.0
print(f'Essas foram as informações trazidas:\n\nQuilos em exesso:{e:.0f}\n\nValor da multa:R${m:.2f}.\n')

os.system('pause')





