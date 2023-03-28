
# Aula de Fila       Significa .append(acrescentar) pop(remover)

#Exercício
fila = [0, 10, 20, 30, 40, 50 ]
fila.append(60)  # insere um elemento no final da fila
fila.append(70)  # insere um elemento no final da fila
fila.append(80)  # insere um elemento no final da fila
fila.append(90)  # insere um elemento no final da fila
fila.append(100) # insere um elemento no final da fila
print(fila)

print( fila.pop(0) )   # remove um elemento no final da fila
print( fila.pop(0) )   # remove um elemento no final da fila
print( fila.pop(0) )   # remove um elemento no final da fila
print( fila.pop(0) )   # remove um elemento no final da fila
print( fila.pop(0) )   # remove um elemento no final da fila
print( fila.pop(0) )   # remove um elemento no final da fila


# Faça um programa de senha para atendimento em um açougue 
# O programa deverá ter funções de:
# - pegar senha
# - mostrar quem esta na fila(senha)
# - chamar senha - [painel]

senha_açougue = []

def add():
    senha_açougue.append(' X ')# insere um elemento no final da fila
    print(senha_açougue)


def rem():
    print(senha_açougue.pop(0) ) # renove um elemento no final da fila
    print(senha_açougue)

while True:
    escolha = int(input('1 para add e 2 para rem'))

    if escolha == 1:
        rem()
    elif escolha == 2:
        rem()
    else:
        print('opcao invalida')

