#Calculo de salário
import os

print('\n\nIremos realizar o calculo para trazer informações do seu salário!\n\n\n')
h = int(input('==> Quantas horas você trabalha durante o mês?\n'))
vh= float(input('\n==> Qual valor da sua hora de trabalho?\n'))
sb =float(h*vh)
print(f'\n\nSalário Bruto: R${sb:.2f}.')
ir = float(sb*11)/100
print(f'\nImposto de Renda (11%): R${ir:.2f}.')
inss = float(sb*8)/100
print(f'\nINSS (8%): R${inss:.2f}.')
sind = float(sb*5)/100
print(f'\nSindicato (5%): R${sind:.2f}.')
total = ir+sind+inss
print(f'\n\nSalário liquido de R${sb-total:.2f}!\n\n')



os.system('pause')