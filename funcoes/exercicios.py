from random import randint
# Atividade sobre funções Python Brasil


def tree():
    n = int(input('Insert a number: '))
    result = [n]
    # for i in range(n):
    #     print('test')


# tree()

# Questão 03
sum = lambda num1, num2, num3: num1 + num2 + num3


# print(sum(1, 1, 1))

# Questão 05
def somaImposto(taxaImposto, custo):
    imposto = (taxaImposto / 100) * custo
    resultado = custo + imposto
    return resultado


# print(f'Calculadora de Imposto\nCusto com imposto: {somaImposto(3, 10)}')


# Questão 07
def calcular():
    prestacao = float(input('Valor da pestação: '))
    atraso = int(input('Quantos dias de atraso? '))
    print(valorPagamento(prestacao, atraso))


def valorPagamento(prestacao, atraso):
    if atraso > 0:
        juros = 0.1 * atraso
        resultado = (prestacao * 00.3) * juros + prestacao
        return resultado
    else:
        juros = 0.1 * atraso
        resultado = prestacao * juros + prestacao
        return resultado


# calcular()

# Questão 08
sizeNumber = lambda number: f'Size of: {len(str(number))}'
#n = sizeNumber(input('Enter a value: '))
#print(n)

# Questão 09
reverse = lambda text: text[::-1]
#txt = reverse(str(input('Insert a value: ')))
#print(txt)

# Questão 10
def craps():
    k = randint(2, 13)
    if k == 7 or k == 11:
        print('Você é o mestre!! Ganhou!!')
    elif k == 2 or k == 3 or k == 12:
        print('Craps!!! Você perdeu!')
    elif k in range(4, 6) or k in range(8, 10):
        print(f'Your number: {k}')
        print('Digite D para jogar o dado: ')
        z = 0
        while k != z:
            print('Digite D para jogar o dado:')
            s = input()
            if s == 'D':
                z = randint(2, 13)
                print('Seu numero foi: ', z)
                if z == 7:
                    print('Voce Perdeu!!!')
                break
                print('Voce Ganhou!!!') if z != 7 else print('Voce Perdeu!!!')

# craps()

# Questão 12
def shuffle(txt):
    






# Questão 11
def validateDate():
    date = str(input('Insert data value: DD.MM.AAAA'))
    pass