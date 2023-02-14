'''

# EXERCÍCIO WHILE(ENQUANTO) IMPRIMINDO DE 1 a 3 com while
x = 1
while x <= 3:
    print (x)
    x = x + 1

x = 1
while x <= 100:
    print (x)
    x = x + 1
   
x = 50
while x <= 100:
    print (x)
    x = x + 1

x = 1
while x <= 3:
    print (x)
    x = x + 1


x = 10
while x > 0:
    print (x)
    x = x - 1
'''
'''
# EXERCÍCIO ACUMULATIVO
N = 1
soma = 0
while N <= 4:
    x = int(input(F'digite o numero'))
    soma = soma + x 
    N = N + 1 


print(f"soma:  {soma}")
'''
#EXERCÍCIO DE INTERROPENDO A REPETIÇÃO
S = 0
while True:
    V = int(input("digite um número a soma ou 0 para sair:"))
    if V==0:
       break
    S = S+V
print(S)

while True:
    n1 = float(input('valor 1:'))
    n2 = float(input('valor 2:'))

    operação = input('escolha a operação')

    if operação == '+':
        resultado = n1 + n2

    elif operação == '-':
        resultado = n1 - n2

    elif operação == '*':
        resultado = n1 * n2

    elif operação == '/':
        resultado = n1 / n2

    else:
        print('opção invalida')

    print(f'o resultado é {resultado} \n')
